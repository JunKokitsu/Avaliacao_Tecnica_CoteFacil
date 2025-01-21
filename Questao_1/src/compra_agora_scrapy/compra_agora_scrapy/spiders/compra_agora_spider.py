from base_spider import BaseSpider
import scrapy

class CompraAgoraSpiderSpider(BaseSpider):
    """
    Spider para extração de categorias e produtos.
    """
    name = "compra_agora_spider"
    start_urls = ["https://www.compra-agora.com/"]
    url_categorias = []

    def parse(self, response):
        """
        Processa a página inicial para encontrar categorias e realiza requisições para a API.

        Args:
            response (scrapy.http.Response): Resposta da página inicial.
        """
        self.url_categorias = self.extract_categories(response)
        self.logger.info("Categorias encontradas: %s", self.url_categorias)
        if not self.url_categorias:
            self.logger.warning("Nenhuma categoria foi encontrada. Spider encerrado.")
            return

        for categoria in self.url_categorias:
            page = 1
            url = f"https://www.compra-agora.com/api/catalogproducts/{categoria}/?p={page}"
            self.headers["Referer"] = f"https://www.compra-agora.com/loja/{categoria}"
            yield scrapy.Request(
                url=url,
                callback=self.parse_paginated_json,
                headers=self.headers,
                meta={"categoria": categoria, "page": page},
            )

    def parse_paginated_json(self, response):
        """
        Processa a resposta JSON da API e extrai informações dos produtos.

        Args:
            response (scrapy.http.Response): Resposta JSON da API.
        """
        categoria = response.meta.get("categoria", "Desconhecida")
        page = response.meta.get("page", 1)
        self.logger.info(f"Processando produtos da categoria: {categoria}, página: {page}")
        
        data = response.json()
        produtos = data.get("produtos", [])

        if not produtos:
            self.logger.info(f"Nenhum produto encontrado na categoria {categoria}, página {page}. Finalizando a categoria.")
            return

        self.logger.info(f"Encontrados {len(produtos)} produtos na categoria {categoria}, página {page}.")
        for idx, produto in enumerate(produtos, start=1):
            variacoes = produto.get("Variacoes", [])
            descricao = (
                variacoes[0].get("Descricao", "Descrição não disponível")
                if variacoes and isinstance(variacoes, list)
                else "Descrição não disponível"
            )
            imagem_url = f"https://images-unilever.ifcshop.com.br/produto/{produto.get('Foto', '')}"

            item = {
                "produto": produto.get("ProdutoId"),
                "Descrição": descricao,
                "Fabricante": produto.get("Fabricante", "Fabricante não disponível"),
                "imagem_url": imagem_url,
            }
            self.logger.info(item)
            yield item

        # Incrementa a página e faz nova requisição
        next_page = page + 1
        next_url = f"https://www.compra-agora.com/api/catalogproducts/{categoria}/?p={next_page}"
        yield scrapy.Request(
            url=next_url,
            callback=self.parse_paginated_json,
            headers=self.headers,
            meta={"categoria": categoria, "page": next_page},
        )
