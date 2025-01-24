import logging
import sys
from decryptor import Decryptor


class CredentialManager:
    """Gerencia a descriptografia e validação das credenciais."""
    def __init__(self, encrypted_credentials, key_base64):
        self.encrypted_credentials = encrypted_credentials
        self.key_base64 = key_base64

    def get_credentials(self):
        decryptor = Decryptor(self.key_base64)
        decrypted = decryptor.decrypt(self.encrypted_credentials).split(",")
        if len(decrypted) != 2 or not all(decrypted):
            logging.error("Credenciais inválidas ou ausentes.")
            sys.exit(1)
        return decrypted
