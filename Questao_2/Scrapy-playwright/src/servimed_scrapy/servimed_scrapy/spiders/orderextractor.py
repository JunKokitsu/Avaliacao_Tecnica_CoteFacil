import logging
import scrapy


class OrderExtractor:
    """Extrai informações do pedido."""
    def __init__(self, order_id):
        self.order_id = order_id

    async def extract_order_info(self, page):
        try:
            pedidos_url = "https://pedidoeletronico.servimed.com.br/pedidos"
            await page.goto(pedidos_url)
            logging.info("Página de pedidos acessada.")
            
            # Confirmar modal
            #confirm_button = await page.query_selector('button.swal2-confirm.swal2-styled')
            confirm_button = await page.wait_for_selector('button.swal2-confirm.swal2-styled', timeout=7000)
            if confirm_button:
                await confirm_button.click()
                logging.info("Modal de confirmação fechado.")
            else:
                logging.info("Modal de confirmação não encontrado, continuando o processo.")

            # Buscar pedido
            await page.fill('input[placeholder*="Digite o código"]', self.order_id)
            await page.click('button.btn.btn-primary')
            await page.wait_for_load_state("networkidle")

            element = await page.query_selector("p.alert.alert-info")
            if element:
                element_text = await element.text_content()
                logging.info(f"mensagem: {element_text}")
                raise Exception("Esse pedido não existe")
            else: 
                logging.info("Pedido buscado com sucesso.")
                
            # Abrir detalhes
            await page.click('button.btn.btn-icon[title="informações do pedido"]')
            logging.info("detalhes.")
            
            
            #espera o modal aparecer
            await page.wait_for_selector('modal-container.modal.fade.show', timeout=7000)
            await page.wait_for_load_state("networkidle")

            html = await page.content()
            return scrapy.http.HtmlResponse(
                url=page.url, body=html, encoding="utf-8"
            )
        except Exception as e:
            logging.error(f"Erro ao extrair informações do pedido: {e}")
            raise
