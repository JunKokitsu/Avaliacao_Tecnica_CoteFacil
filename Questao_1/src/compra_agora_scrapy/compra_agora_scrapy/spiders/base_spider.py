import scrapy
import logging

class BaseSpider(scrapy.Spider):
    """
    Classe base para spiders com lógica compartilhada.
    """
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    def extract_categories(self, response):
        """
        Extrai as categorias do elemento <nav> com o ID especificado.

        Args:
            response (scrapy.http.Response): A resposta da página inicial.

        Returns:
            list: Lista de categorias extraídas.
        """
        self.logger.info("Procurando categorias no elemento <nav>...")
        nav = response.xpath("//nav[@id='carousel-categories-home']")
        if not nav:
            self.logger.warning("Elemento <nav id='carousel-categories-home'> não encontrado.")
            return []

        base_url = "https://www.compra-agora.com/loja/"
        
        categories = [
            href.replace(base_url, "").strip()
            for href in nav.xpath(".//a/@href").getall()
            if href.startswith(base_url)
        ]

        excluir_categoria = ["destaques", "naturais-e-nutricao", "novidades"]

        categories = [
            cat for cat in categories
            if not any(valor in cat for valor in excluir_categoria)
        ]
        return categories
