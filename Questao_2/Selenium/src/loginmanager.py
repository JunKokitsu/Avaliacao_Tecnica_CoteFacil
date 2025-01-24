import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginManager:
    def __init__(self, driver):
        self.driver = driver

    def login(self, url, username, password):
        logging.info("Acessando a página de login.")
        self.driver.get(url)

        try:
            form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'form.form-signin'))
            )
            logging.info('Formulário de login localizado.')

            form.find_element(By.NAME, "username").send_keys(username)
            form.find_element(By.NAME, "password").send_keys(password)

            form.find_element(By.CSS_SELECTOR, "button.btn.btn-block.btn-success").click()
            logging.info('Login realizado com sucesso.')

            try:
               
                confirm_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-confirm.swal2-styled'))
                )
                confirm_button.click()
                logging.info('Confirmação do modal realizada com sucesso.')
            except TimeoutException:
                
                logging.info('modal versão não encontrado, continuando o processo.')

        except Exception as e:
            logging.error(f"Erro durante o login: {e}")
            raise
