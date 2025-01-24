import logging
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataExtractor:
    def __init__(self, driver):
        self.driver = driver

    def extract_table_data(self):
        try:
            # Aguarda o modal aparecer
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "modal-container.modal.fade.show"))
            )
            logging.info('Modal localizado com sucesso.')

            # Verifica se o elemento "Motivo da Rejeição" existe
            div_motivo_rejeicao_elements = modal.find_elements(By.XPATH, "//label[text()='Motivo da Rejeição']/parent::div")
            if div_motivo_rejeicao_elements:
                div_motivo_rejeicao = div_motivo_rejeicao_elements[0]
                input_motivo_rejeicao = div_motivo_rejeicao.find_element(By.CSS_SELECTOR, "input.form-control")
                motivo_rejeicao = input_motivo_rejeicao.get_attribute('value')
                logging.info(f"Motivo de rejeição: {motivo_rejeicao}")
            else:
                motivo_rejeicao = None
                logging.warning("Elemento 'Motivo da Rejeição' não encontrado.")

            # Extrai a tabela
            table = modal.find_element(By.CSS_SELECTOR, "div.modal-body table.table")
            headers = table.find_elements(By.CSS_SELECTOR, "thead th")
            header_positions = {
                header.text: idx for idx, header in enumerate(headers) if header.text in ["Código", "Descrição", "Qtd. Faturada"]
            }

            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
            itens = []
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                itens.append({
                    "Código": cells[header_positions["Código"]].text if "Código" in header_positions else "N/A",
                    "Descrição": cells[header_positions["Descrição"]].text if "Descrição" in header_positions else "N/A",
                    "Qtd. Faturada": cells[header_positions["Qtd. Faturada"]].text if "Qtd. Faturada" in header_positions else "N/A"
                })

            output = {
                "Motivo": motivo_rejeicao,
                "Itens": itens
            }
            logging.info('Dados extraídos com sucesso.')
            return output

        except Exception as e:
            logging.error(f"Erro ao extrair os dados da tabela: {e}")
            raise

    def save_data_to_json(self, data, filename='results.json'):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logging.info(f'Dados salvos no arquivo {filename} com sucesso.')
        except Exception as e:
            logging.error(f"Erro ao salvar os dados no arquivo JSON: {e}")
            raise
