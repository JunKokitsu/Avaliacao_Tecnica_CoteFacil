# Avaliacao_Tecnica_CoteFacil
Avaliação técnica do processo seletivo da Cote Fácil.

## Questão 1

Desenvolva um script que interaja com o website https://www.compra-agora.com. Para realizar este processo você pode escolher entre as bibliotecas Requests ou Scrapy.  Ao final da execução do script deve ser gerado um arquivo JSON contendo os dados obtidos.

#### Tópicos:
  1. Efetuar o login
     
  2. Entre em cada categoria:
     
  ![Captura de tela 2025-01-24 181736](https://github.com/user-attachments/assets/b1a82b95-5889-49e0-82b1-c17a221eab85)
 
  4. Capture as seguintes dados de todos os produtos disponíveis: Descrição, Fabricante e URL da imagem no formato JSON.
   
### Login

Tópico 1 do roteiro da questão 1.

#### Programa web scraper desenvolvido com Requests e BeatifulSoup para efetuar o login no site compra-agora.com.

#### Estrutura:

main.py: executa o programa com Python main.py

scraper.py: Identifica os elementos HTML e interage com a pagina adicionando nos campos <input> username e <input> password seus respectivos valores e 'passando' no recaptchav2 para o envio do formúlario.

decryptor.py: faz o gerenciamento da criptografia das credenciais.

#### Como executar a aplicação Login da questão 1:

##### Executar o programa:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:  
  
    docker-compose up --build -d login_app //este comando irá executar o programa que fará o login

##### acessar os logs da execução do programa em tempo real:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose logs -f login_app

##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down

### Extração de dados
Tópico 2 e 3 do roteiro da questão 1.

#### Programa web scraper desenvolvido com Scrapy para extrair todos os produtos do site compra-agora.com pela api no formato JSON.

#### Estrutura:

main.py: executa o Spider principal com Python main.py.

compra_agora_spider.py: Spider responsável por extrair categorias, coletar produtos da API e gerenciar paginação.

base_spider.py: Classe base com lógica compartilhada, incluindo configuração de headers e extração de categorias.


#### Como executar a aplicação Extração dos dados da questão 1

##### Executar o programa:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose up --build -d extracao_dados_app // este comando irá executar o programa que fará a extração dos dados.

##### acessar os logs da execução do programa em tempo real: 
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose logs -f extracao_dados_app

##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down

#### Desafios:

  - não foi possível validar o captcha no login.


## Questão 2

A solução deve ser implementada utilizando a linguagem Python na versão 3.6+ e a biblioteca usada deve ser Scrapy. O script deve realizar processo de obter o retorno de faturamento do pedido que o usuário der entrada. 

#### Tópicos:
  1. Efetue login no site usando os dados acima;
     
  2. Vá em “Meus Pedidos”;
     
  3. Pesquise o pedido que o usuário inputou nos argumentos do script. Traga o retorno de faturamento no formato json contendo os campos: Motivo, itens [codigo_produto, descricao, quantidade_faturada]. Retorne um erro caso não o encontre o pedido no site.
     

#### Programa web scraper desenvolvido com Scrapy e Scrapy-Playwright que faz o login, interage com a página e faz a extração dos pedidos do site servimed.com.

#### Estrutura:

main.py: executa o Spider principal com Python main.py <código_do_pedido>.

login.py: Interage com a página de login, insere as credenciais nos <input>'s envia o formulário para executar o login.

orderextractor.py: Interage com o site e busca o pedido depois de efetuar o login.

orders.py: Faz a extração dos dados do pedido.

credentialmanager.py: gerencia a descriptografia e a validação das crendencias na hora do login.

decryptor.py: faz o gerenciamento da criptografia das credenciais.


#### Como executar a aplicação Extração dos dados da questão 1

##### Executar o programa:
  Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
        
    docker-compose up --build -d extract_pedidos_app
  
  Depois execute o comando para interagir no container:
  
    docker exec -it avaliacao_tecnica_cotefacil-extract_pedidos_app-1 bash

  Execute o programa:
  
    python main.py <código_do_pedio>

##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down

### Adicional da Questão 2

Existe outra aplicação feita em Selenium, nela o output consegue pegar o Motivo do pedido.

ps.: precisa ser executado com o ambiente virtual.

#### Desafios:

  - Em scrapy não foi possível pegar o valor do <input> Motivo dentro do modal detalhes. Retornando NULL todas as execuções.
    

## Questão 3

Escreva um script Python que recebe como parametro um número n inteiro positivo e imprime no console o n-ésimo valor correspondente da sequencia de Fibonacci. Obs.: O problema deve ser resolvido utilizando recursão. 

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


## Questão 4

Explique o problema que poderia acontecer com o programa desenvolvido na questão 1 ao passar como entrada n = 50.


O algoritmo mais simples para cálculo da série de Fibonacci usando recursão se baseia na criação de uma função recursiva que chama quantas vezes forem necessárias até que se atinja o caso base, F(0) ou F(1). O programa fibonacci.py desenvolvido na questão 4 é um exemplo desse algoritmo. Desta forma, problemas menores mas idênticos, são executados de forma repetida, tornando a computação mais pesada conforme n fica maior (complexidade na ordem de 2^n). O tempo de execução cresce exponencialmente porque a função calcula muitos subprocessos idênticos repetidamente. Quando passamos o valor 50 como parâmetro, o script vai demorar muito tempo para executar ou até nem executar, dependendo da capacidade da máquina.

Uma forma de tornar o algoritmo recursivo mais eficiente é armazenando os resultados de chamadas anteriores em uma variável do tipo lista. Assim, quando uma mesma entrada ocorre novamente, basta procurar o resultado correspondente no vetor e retorná-lo, sem precisar executar novamente, reduzindo a complexidade de tempo de execução de O(2^n) para O(n).


## Questão 5

Sobre a infraestrutura de serviços da Amazon Web Services, explique a relação entre Virtual Private 
Networks, Subnets e Security Groups.

A Amazon Web Services (AWS) oferece serviços de infraestrutura de redes baseados em nuvem que auxiliam no projeto e no gerenciamento dos recursos de rede. Três componentes importantes da rede da AWS são: Virtual Private Cloud (VPC), Subnets e Security Groups.

#### Virtual Private Network da AWS (VPC)

Uma VPC é uma rede virtual privada logicamente isolada dentro de uma região da AWS. Ela permite a definição de faixas de endereços IP, a configuração de tabelas de roteamento, gateways de internet e políticas de controle de acesso. Portanto, a VPC abrange toda a infraestrutura onde subnets, gateways e security groups coexistem.

A rede virtual privada da AWS fornece uma seção logicamente isolada da nuvem AWS, onde instâncias da AWS, como a EC2 (Amazon Elastic Compute Cloud), podem ser iniciadas. A EC2 é um serviço da AWS que fornece capacidade computacional na nuvem.

#### Subnet

Uma Subnet é uma subdivisão da rede dentro da VPC, com uma faixa de endereços IP previamente definida, podendo ser pública (com acesso à internet via gateway), privada (sem rota direta à internet exigindo um NAT para acesso à internet pública), somente VPN (site-to-site VPN) ou isolada (acesso somente na própria VPC). O objetivo da Subnet é organizar os recursos dentro da VPC e controlar a conectividade entre os recursos com base nas tabelas de roteamento associadas. As Subnets dividem logicamente os recursos dentro da VPC em zonas de disponibilidade de modo a atingir alta disponibilidade e tolerância a falhas.

A VPC fornece a rede virtual onde as instâncias e outros recursos da AWS operam, enquanto as Subnets dividem essa rede em segmentos específicos, permitindo o controle de tráfego em nível granular. 

#### Security Groups

Um Security Group é um conjunto de regras que controla o tráfego de entrada e saída de instâncias ou recursos específicos em uma subnet. Ele atua como um firewall virtual, definindo regras para permitir ou negar o tráfego baseado em protocolos, portas e endereços IP, aplicando as regras a nível de instâncias EC2, por exemplo, independentemente da configuração da subnet.

O Security Group é stateful, ou seja, se o tráfego de entrada for permitido por uma regra, as respostas ao tráfego de saída são automaticamente permitidas e vice-versa.

Security Groups não se aplicam globalmente na VPC ou às subnets. Cada instância ou recurso pode ter vários Security Groups associados.

 
Portanto, uma VPC é o contêiner maior que engloba todas as Subnets e Security Groups. As Subnets dividem logicamente os recursos dentro da VPC em zonas de disponibilidade e controlam o tráfego externo através de tabelas de roteamento. Os Security Groups protegem instâncias e recursos específicos das Subnets, permitindo a granularidade das regras de acesso.




