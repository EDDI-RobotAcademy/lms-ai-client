import os
import base64
import httpx
from fastapi import HTTPException
from dotenv import load_dotenv
from openai import OpenAI
from openai_chatbot_domain.repository.openai_chatbot_domain_repository import OpenaiChatbotDomainRepository

load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다!')

client = OpenAI()

class OpenaiChatbotDomainRepositoryImpl(OpenaiChatbotDomainRepository):
    __instance = None

    headers = {
        'Authorization': f'Bearer {openaiApiKey}',
        'Content-Type': 'application/json'
    }

    OPENAI_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def generateRecipe(self, userSendMessage):
        data = {
            'model': 'gpt-4o-mini',
            'messages': [
                {"role": "system", "content": "You are a helpful assistant. 한글로 답변하자.!"},
                {"role": "user", "content": userSendMessage}
            ]
        }
        print("Recipe generating starting...")

        async with httpx.AsyncClient(timeout=10) as client:
            try:
                response = await client.post(self.OPENAI_CHAT_COMPLETIONS_URL, headers=self.headers, json=data)
                response.raise_for_status()

                generatedRecipe = response.json()['choices'][0]['message']['content'].strip()
                print(generatedRecipe)
                return {"recipe": generatedRecipe}

            except httpx.HTTPStatusError as e:
                print(f"HTTP Error: {str(e)}")
                print(f"Status Code: {e.response.status_code}")
                print(f"Response Text: {e.response.text}")
                raise HTTPException(status_code=e.response.status_code, detail=f"HTTP Error: {e}")

            except (httpx.RequestError, ValueError) as e:
                print(f"Request Error: {e}")
                raise HTTPException(status_code=500, detail=f"Request Error: {e}")


    async def getGeneratedVoice(self, chatbotMessage, voiceActor):
        response = client.audio.speech.create(
            model="tts-1",
            voice=voiceActor,
            input=chatbotMessage,
        )
        audioData = base64.b64encode(response.content).decode('utf-8')
        return audioData
