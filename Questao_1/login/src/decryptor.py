import logging
import base64
from nacl import secret


class Decryptor:
    """Classe responsável por lidar com a criptografia e descriptografia."""

    def __init__(self, key_base64: str):
        self.key = base64.b64decode(key_base64)
        self.box = secret.SecretBox(self.key)

    def decrypt(self, encrypted_base64: str) -> str:
        try:
            encrypted = base64.b64decode(encrypted_base64)
            decrypted = self.box.decrypt(encrypted).decode()
            return decrypted
        except Exception as e:
            logging.critical(f"Erro ao descriptografar os dados: {e}")
            raise
