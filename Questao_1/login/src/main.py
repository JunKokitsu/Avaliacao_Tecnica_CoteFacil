import logging
import sys
from decryptor import Decryptor
from scraper import WebScraper

# Configurando o logger para suportar UTF-8
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout,  # Define saída padrão como UTF-8
    encoding="utf-8"    # Configura codificação UTF-8
)

if __name__ == "__main__":
    # Configuração inicial
    key_base64 = "/Fl3a4e/Ownrn1/z3skOQSJqC2Hg6RNMaW0xA9gylhw="
    encrypted_credentials = (
        "EDuN9RxebI1h5shmF6CawIGdloZDtTfnScmXDE2hvtJ0mdy6lLDmSxISCTgkeiYPCUrB3nOcFXu2C3RszYyOuTwHmg=="
    )

    # Inicializando o descriptografador
    decryptor = Decryptor(key_base64)
    decrypted_credentials = decryptor.decrypt(encrypted_credentials).split(",")

    # Inicializando o scraper
    url = "https://www.compra-agora.com"
    captcha_api_key = "SUA_CHAVE_API_CAPTCHA"
    scraper = WebScraper(url, decrypted_credentials, captcha_api_key)

    # Submissão do formulário
    try:
        soup_post = scraper.submit_form()
        if soup_post:
            user_span = soup_post.find("span", {"class": "nome-usuario"})
            nome_usuario = user_span.get_text(strip=True)
            if "login" in nome_usuario.lower() or "cadastre-se" in nome_usuario.lower():
                logging.warning("Não foi possível acessar a conta.")
            else:
                logging.info("Login executado com sucesso! ", nome_usuario )

    except Exception as e:
        logging.critical(f"Erro durante a execução: {e}")
