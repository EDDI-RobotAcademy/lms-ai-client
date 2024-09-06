import sys
import os
from template.request_generator.base_request import BaseRequest

sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'template'))

from user_defined_protocol.protocol import UserDefinedProtocolNumber

class ChatlogRequest(BaseRequest):
    def __init__(self, account_id: str, recipe: str, recipe_hash: str):
        self.protocolNumber = UserDefinedProtocolNumber.SAVE_CHAT_LOG.value
        self.account_id = account_id
        self.recipe = recipe
        self.recipe_hash = recipe_hash

    def to_dict(self):
        return {
            "protocolNumber": self.protocolNumber,
            "account_id": self.account_id,
            "recipe": self.recipe,
            "recipe_hash": self.recipe_hash,
        }

    def __str__(self):
        return f"ChatlogRequest(account_id={self.account_id}, recipe={self.recipe}, recipe_hash={self.recipe_hash})"
