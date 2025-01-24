# Avaliacao_Tecnica_CoteFacil
Avaliação técnica do processo seletivo da Cote Fácil.

## Questão 1
#### Desafio:
  Desenvolva um script que interaja com o website https://www.compra-agora.com. Para realizar este 
  
processo você pode escolher entre as bibliotecas Requests ou Scrapy.  Ao final da execução do script deve 

ser gerado um arquivo JSON contendo os dados obtidos.

#### Tópicos:
  1. Efetuar o login
     
  2. Entre em cada categoria:
     
    ![image](https://github.com/user-attachments/assets/2aa881b9-08da-4098-af81-2feaa8943801)

     
  4. Capture as seguintes dados de todos os produtos disponíveis: Descrição, Fabricante e URL da imagem no formato JSON.
   
###Login

Tópico 1 do roteiro da questão 1.

#### Programa web scraper desenvolvido com Requests e BeatifulSoup para efetuar o login no site compra-agora.com.

#### Estrutura:

main.py: executa o programa com Python main.py

scraper.py: Identifica os elementos HTML e interage com a pagina adicionando nos campos <input> username e <input> password seus respectivos valores e 'passando' no recaptchav2 para o envio do formúlario.

decryptor.py: faz o gerenciamento da criptografia das credenciais.

Como executar a aplicação Login da questão 1:


###Extração de dados
Tópico 2 e 3 do roteiro da questão 1.

#### Programa web scraper desenvolvido com Scrapy para extrair todos os produtos do site compra-agora.com pela api no formato JSON.

#### Estrutura:

main.py: executa o Spider principal com Python main.py.

compra_agora_spider.py: Spider responsável por extrair categorias, coletar produtos da API e gerenciar paginação.

base_spider.py: Classe base com lógica compartilhada, incluindo configuração de headers e extração de categorias.


#### Como executar a aplicação Extração dos dados da questão 1

##### Executar o programa:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose up --build -d login_app //este comando irá executar o programa que fará o login

  ##### acessar os logs da execução do programa em tempo real:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose logs -f login_app

  ##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down

##### Executar o programa:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose up --build -d extracao_dados_app // este comando irá executar o programa que fará a extração dos dados.

##### acessar os logs da execução do programa em tempo real: 
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose logs -f extracao_dados_app

  ##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down




## Questão 3

#### A sequência de Fibonacci é uma série de números naturais em que cada número é a soma dos dois anteriores, começando com 0 e 1. Portanto, a sequência é formada pelos números: 0, 1, 1, 2, 3, 5, 8, 13, 21 e assim por diante. Na terminologia matemática, esta série representa um problema clássico de recursão, uma vez que cada termo da sequência é uma função dos termos precedentes:

F(0) = 0

F(1) = 1

F(2) = F(1) + F(0) 

...

F(n) = F(n-1) + F(n-2) 

#### Programa python para cálculo do n-ésimo termo da série de Fibonacci usando recursão:

### Como executar o programa:

#### Para executar digitar: python fibonacci.py 20

Onde fibonacci.py é o nome do programa python e 20 corresponde à posição do termo na sequência de Fibonacci.



