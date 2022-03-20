from cryptography.fernet import Fernet
from src.common.conf import *


class Encryptor:
    def __init__(self):
        self.impl = Fernet(ENCRYPTION_KEY.encode())

    def encode(self, data: str) -> str:
        return self.impl.encrypt(data.encode()).decode()

    def decode(self, data: str) -> str:
        return self.impl.decrypt(data.encode()).decode()
