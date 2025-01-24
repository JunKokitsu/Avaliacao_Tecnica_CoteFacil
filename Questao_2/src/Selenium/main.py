import os
import sys
import json
import logging
from projectbase import ProjectBase
from loginmanager import LoginManager
from ordersearcher import OrderSearcher
from dataextractor import DataExtractor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Questao2Spider:
    def __init__(self, username, password, order_id):
        self.driver_manager = ProjectBase()
        self.login_manager = LoginManager(self.driver_manager.driver)
        self.order_searcher = OrderSearcher(self.driver_manager.driver)
        self.data_extractor = DataExtractor(self.driver_manager.driver)
        self.username = username
        self.password = password
        self.order_id = order_id

    def run(self):
        try:
            self.login_manager.login("https://pedidoeletronico.servimed.com.br/login", self.username, self.password)
            self.order_searcher.search_order(self.order_id)
            data = self.data_extractor.extract_table_data()
            self.data_extractor.save_data_to_json(data)
            logging.info(json.dumps(data, ensure_ascii=False, indent=4))
        finally:
            self.driver_manager.quit_driver()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Uso: python main.py <order_id>")
        sys.exit(1)

    order_id = sys.argv[1]
    username = ""
    password = ""

    if not username or not password:
        logging.error("Credenciais não encontradas nas variáveis de ambiente.")
        sys.exit(1)

    init = Questao2Spider(username, password, order_id)
    init.run()
