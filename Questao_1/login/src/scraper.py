import logging
import requests
import time
from bs4 import BeautifulSoup

class WebScraper:
    """Classe principal para realizar o scraping e envio de formulário."""

    def __init__(self, url: str, credentials: list[str], captcha_api_key: str):
        self.url = url
        self.credentials = credentials
        self.captcha_api_key = captcha_api_key

    def fetch_page(self) -> bytes:
        """Realiza uma requisição GET para buscar o conteúdo da página."""
        try:
            logging.info("Enviando requisição GET para a URL.")
            response = requests.get(self.url)
            response.raise_for_status()
            logging.info("Página carregada com sucesso.")
            return response.content
        except requests.RequestException as e:
            logging.critical(f"Erro ao carregar a página: {e}")
            raise

    def solve_captcha(self, site_key: str) -> str:
        """Resolve o CAPTCHA usando a API do 2Captcha."""
        try:
            logging.info("Enviando CAPTCHA para resolução no 2Captcha.")
            captcha_response = requests.post(
                "http://2captcha.com/in.php",
                data={
                    "key": self.captcha_api_key,
                    "method": "userrecaptcha",
                    "googlekey": site_key,
                    "pageurl": self.url
                }
            )
            if "OK" not in captcha_response.text:
                logging.error("Erro ao enviar CAPTCHA ao 2Captcha")
                return None

            captcha_id = captcha_response.text.split('|')[1]

            logging.info("Aguardando solução do CAPTCHA...")
            while True:
                solution_response = requests.get(
                    f"http://2captcha.com/res.php?key={self.captcha_api_key}&action=get&id={captcha_id}"
                )
                if solution_response.text == "CAPCHA_NOT_READY":
                    time.sleep(5)
                    continue
                if "OK" in solution_response.text:
                    logging.info("CAPTCHA resolvido com sucesso")
                    return solution_response.text.split('|')[1]

                logging.error("Erro ao obter solução do CAPTCHA.")
                return None
        except Exception as e:
            logging.error(f"Erro ao resolver CAPTCHA: {e}")
            return None

    def submit_form(self) -> BeautifulSoup:
        """Busca o formulário na página, preenche os campos, envia o formulário e resolve o CAPTCHA."""
        try:
            page_content = self.fetch_page()
            soup = BeautifulSoup(page_content, "html.parser")

            logging.info("Procurando div com ID login-cadastro")
            div = soup.find("div", {"id": "login-cadastro"})
            if not div:
                logging.error("Div com ID login-cadastro não encontrada")
                return None

            logging.info("Div encontrada")
            form = div.find("form")
            if not form:
                logging.error("Formulário não encontrado")
                return None

            logging.info("Procurando campos do formulário...")
            input_user = form.find('input', {'id': 'usuarioCnpj'})
            input_password = form.find('input', {'id': 'usuarioSenhaCA'})

            if not input_user or not input_password:
                logging.error("Campos do formulário não encontrados")
                return None

            username, password = self.credentials
            input_user["value"] = username
            input_password["value"] = password

            # Resolver CAPTCHA se necessário
            site_key = soup.find("div", {"data-sitekey": True})
            if site_key:
                captcha_solution = self.solve_captcha(site_key["data-sitekey"])
                if captcha_solution:
                    logging.info("CAPTCHA resolvido e enviado.")
                else:
                    logging.warning("Não foi possível resolver o CAPTCHA.")

            logging.info("Enviando formulário via POST.")
            post_response = requests.post(self.url, data=soup.encode())
            post_response.raise_for_status()

            logging.info("Formulário enviado com sucesso.")
            soup_post = BeautifulSoup(post_response.content, 'html.parser')

            return soup_post
        except Exception as e:
            logging.critical(f"Erro ao processar o formulário: {e}")
            raise
