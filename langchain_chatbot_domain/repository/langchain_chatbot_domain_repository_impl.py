import json
import os
from operator import itemgetter
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import ChatMessageHistory

from langchain_chatbot_domain.repository.langchain_chatbot_domain_repository import LangchainChatbotDomainRepository

load_dotenv()
openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다!')

class LangchainChatbotDomainRepositoryImpl(LangchainChatbotDomainRepository):
    store = {}
    FAISS_INDEX_PATH = "assets/faiss_index_file"

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def loadDocumentation(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            qa_data = json.load(f)

        documents = []
        for item in qa_data:
            question = item['question']
            answer = item['answer']
            documents.append(f"Question: {question}\nAnswer: {answer}")
        return documents

    def generatePrompt(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "당신은 주어진 재료를 기반으로 레시피를 생성하는 챗봇입니다. 질문에 대한 답변을 제공해 주세요. "
                    "[레시피 명], [요리 인분 수], [재료], [요리 과정]을 []를 사용하여 명시해 주세요.",
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        return prompt

    def loadEmbeddingModel(self):
        embedding = OpenAIEmbeddings()
        # embedding = SentenceTransformer('all-MiniLM-L6-v2')
        return embedding

    async def createFaissIndex(self, texts, embedding):
        faissIndex = FAISS.from_texts(texts=texts, embedding=embedding)
        faissIndex.save_local(self.FAISS_INDEX_PATH)

    def loadFaissIndex(self, faissIndexPath, embeddings):
        faissIndex = FAISS.load_local(folder_path=faissIndexPath, embeddings=embeddings, allow_dangerous_deserialization=True)
        return faissIndex

    def loadLLMChain(self):
        return ChatOpenAI(model="gpt-4")

    def get_session_history(self, session_ids='always_same'):
        # print(f"[대화 세션ID]: {session_ids}")
        if session_ids not in self.store:
            self.store[session_ids] = ChatMessageHistory()
        return self.store[session_ids]

    def createChain(self, llm, prompt, faiss_index):
        chain = (
                {
                    "context": itemgetter("question") | faiss_index.as_retriever(), # retriever
                    "question": itemgetter("question"),
                    "chat_history": itemgetter("chat_history"),
                }
                | prompt # 프롬프트 추가
                | llm
                | StrOutputParser() # 언어 모델의 출력을 문자열로 변환
        )

        qa_chain = RunnableWithMessageHistory(
            chain,
            self.get_session_history,
            input_messages_key="question",  # 사용자의 질문이 템플릿 변수에 들어갈 key
            history_messages_key="chat_history",  # 기록 메시지의 키
        )

        return qa_chain

    async def invokeChain(self, chain, userSendMessage):
        result = chain.invoke({"question": userSendMessage},
                              config={"configurable": {"session_id": "always_same"}})
        return result