from src.common.encryptor import Encryptor

e = Encryptor()
a = e.encode('Hello!')
print(a)
print(e.decode(a))
