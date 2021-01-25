from cryptography.fernet import Fernet

def decrypt(arg):
	secret_key = ""
	cipher_suite = Fernet(secret_key)
	return cipher_suite.decrypt(arg)


def encrypt(arg):
	secret_key = ""
	cipher_suite = Fernet(secret_key)
	return str(cipher_suite.encrypt(bytes(arg,"utf-8")))