import json

class JsonWriterPipeline:
    # Pipeline para salvar os itens em um arquivo JSON ao final da execução.
    def open_spider(self, spider):
        #Abre o arquivo JSON ao iniciar o spider.
        self.file = open("resultados.json", "w", encoding="utf-8")
        self.file.write("[\n")  # Inicia o arquivo com uma lista JSON

    def close_spider(self, spider):
        # Fecha o arquivo JSON ao encerrar o spider.
        self.file.write("\n]")  # Fecha a lista JSON
        self.file.close()

    def process_item(self, item, spider):
        # Escreve cada item no arquivo JSON.
        line = json.dumps(item, ensure_ascii=False) + ",\n"  # Converte o item para JSON
        self.file.write(line)  # Escreve no arquivo
        return item
