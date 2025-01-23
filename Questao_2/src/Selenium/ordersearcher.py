import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderSearcher:
    def __init__(self, driver):
        self.driver = driver

    def search_order(self, order_id):
        try:
            pedidos_url = "https://pedidoeletronico.servimed.com.br/pedidos"
            self.driver.get(pedidos_url)

            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control[placeholder*='Digite o código']"))
            )
            input_field.clear()
            input_field.send_keys(order_id)
            logging.info(f'Pedido {order_id} inserido no campo de busca.')

            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
            )
            search_button.click()

            # Verifica se o <p> com o texto de alerta está presente
            try:
                alert_message = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "p.alert.alert-info"))
                )
                alert_text = alert_message.text
                logging.info(f"Mensagem de alerta encontrada: {alert_text}")
            except Exception:
                logging.info("Nenhuma mensagem de alerta encontrada, continuando execução.")

            # Continua execução normal
            order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-icon[title='informações do pedido']"))
            )
            order_button.click()
            logging.info('Botão de informações do pedido clicado com sucesso.')

        except Exception as e:
            logging.error(f"Erro durante a busca do pedido: {e}")
            raise

            

        
