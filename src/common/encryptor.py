from Crypto.Cipher import DES
from src.common.conf import *


class Encryptor:
    def __init__(self):
        self.impl = DES.new(ENCRYPTION_KEY, DES.MODE_ECB)

    def encode(self, data):
        return self.impl.encrypt(self._pad(data.strip().encode())).decode()

    def decode(self, data):
        return self.impl.decrypt(data.encode()).strip().decode()

    def _pad(self, text):
        while len(text) % 8 != 0:
            text += b' '
        return text
