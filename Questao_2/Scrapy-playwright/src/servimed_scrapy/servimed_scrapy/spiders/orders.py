import scrapy
import logging
import json
from credentialmanager import CredentialManager
from login import Login
from orderextractor import OrderExtractor


class orderSpider(scrapy.Spider):
    custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,  # Certifique-se de que está como True
        },
    }
    name = "servimed_spider"

    def __init__(self, order_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        key_base64 = "FNtN72d3EtAyiiw8ZvBR6XhlrwUmOE6dmPM9+4fmPto="
        encrypted_credentials = (
            "CplQqiOlXLizjOLdZPYGaW1rPgzEJQw7EfUZaxF518A4SwmxSKMkVCQ0ej2uqU3ZPW2dY1HsZGW/ROc46m1y6SHn2u1LjgRoheC+d8BxgA=="
        )

        credentials_manager = CredentialManager(encrypted_credentials, key_base64)
        username, password = credentials_manager.get_credentials()

        self.login_handler = Login(username, password)
        self.order_extractor = OrderExtractor(order_id)

    def start_requests(self):
        url = "https://pedidoeletronico.servimed.com.br/login"
        yield scrapy.Request(
            url,
            meta={"playwright": True, "playwright_include_page": True},
            callback=self.handle_login
        )

    async def handle_login(self, response):
        page = response.meta["playwright_page"]
        #logging.info('page', page)
        try:
            await self.login_handler.login(page)
            scrapy_response = await self.order_extractor.extract_order_info(page)
            self.extract_table_data(scrapy_response)
        except Exception as e:
            logging.error(f"Erro no fluxo principal: {e}")
        finally:
            await page.close()

    def extract_table_data(self, response):
        try:
            # Busca o motivo
            div_motivo_rejeicao = response.xpath("//label[text()='Motivo da Rejeição']/parent::div")
            if div_motivo_rejeicao:
                input_motivo_rejeicao = div_motivo_rejeicao.xpath(".//input[@class='form-control']")
                motivo_rejeicao = input_motivo_rejeicao.xpath("@value").get()
                if motivo_rejeicao:
                    logging.info(f"Motivo de rejeição: {motivo_rejeicao}")
                else:
                    logging.warning("Campo de input encontrado, mas sem valor.")
            else:
                logging.warning("Elemento 'Motivo da Rejeição' não encontrado.")

            # Extração da tabela de itens
            itens = []
            for row in response.css("div.modal-body table.table tbody tr"):
                cells = row.css("td::text").getall()
                if len(cells) >= 3:
                    itens.append({
                        "Código": cells[0],
                        "Descrição": cells[1],
                        "Qtd. Faturada": cells[2],
                    })

            output = {"Motivo": motivo_rejeicao, "Itens": itens}
            self.save_data_to_json(output)
            logging.info('------------------------------------------------------------------------------RESULTADO------------------------------------------------------------------------------------')
            logging.info(output)
            logging.info('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        except Exception as e:
            logging.error(f"Erro ao extrair dados: {e}")

    def save_data_to_json(self, data, filename="results.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logging.info(f"Dados salvos em {filename}.")
        except Exception as e:
            logging.error(f"Erro ao salvar dados: {e}")
