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
            confirm_button = await page.query_selector('button.swal2-confirm.swal2-styled')
            if confirm_button:
                await confirm_button.click()
                logging.info("Modal de confirmação fechado.")

            # Buscar pedido
            await page.fill('input[placeholder*="Digite o código"]', self.order_id)
            await page.click('button.btn.btn-primary')
            await page.wait_for_load_state("networkidle")
            logging.info("Pedido buscado com sucesso.")

            # Abrir detalhes
            await page.click('button.btn.btn-icon[title="informações do pedido"]')
            await page.wait_for_load_state("networkidle")
            html = await page.content()
            return scrapy.http.HtmlResponse(
                url=page.url, body=html, encoding="utf-8"
            )
        except Exception as e:
            logging.error(f"Erro ao extrair informações do pedido: {e}")
            raise
