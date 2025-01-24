# Avaliacao_Tecnica_CoteFacil
Avaliação técnica do processo seletivo da Cote Fácil.

## Questão 1

Desenvolva um script que interaja com o website https://www.compra-agora.com. Para realizar este processo você pode escolher entre as bibliotecas Requests ou Scrapy.  Ao final da execução do script deve ser gerado um arquivo JSON contendo os dados obtidos.

#### Tópicos:
  1. Efetuar o login
     
  2. Entre em cada categoria:
     
  ![Captura de tela 2025-01-24 181736](https://github.com/user-attachments/assets/b1a82b95-5889-49e0-82b1-c17a221eab85)
 
  3. Capture as seguintes dados de todos os produtos disponíveis: Descrição, Fabricante e URL da imagem no formato JSON.
   
### Efetuando o Login no site compra-agora.com

Resolução do tópico 1 da questão 1.

#### Este projeto tem como objetivo simular um login automático no site compra-agora.com, que inclui o desafio de lidar com CAPTCHAs. Para a resolução dos CAPTCHAs, o projeto utiliza a integração com o serviço de terceiros 2captcha. O programa realiza a criptografia dos dados de login e simula o processo de autenticação, mas não conclui totalmente a operação, pois a contratação efetiva do serviço 2captcha não foi realizada. 

A aplicação Python carrega páginas web utilizando Requests e BeautifulSoup, preenche o formulário de login com as credenciais criptografadas, simula a integração da API do serviço 2Captcha para resolver o reCAPTCHA e submete o formulário.


#### Como executar a aplicação Login da questão 1:


Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:  
  
    docker-compose up --build -d login_app //este comando irá executar o programa que fará o login

##### acessar os logs da execução do programa em tempo real:
Para acessar os logs da execução, digitar:  
  
    docker-compose logs -f login_app

##### parar a execução da aplicação:
No diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down


### Extração de dados do site www.compra-agora.com
Resolucação dos tópicos 2 e 3 da questão 1.

#### Este projeto utiliza Scrapy para realizar a coleta de categorias e produtos do site Compra-Agora.com, incluindo o consumo de uma API que retorna informações detalhadas sobre os produtos em formato JSON.

Começa pela identificação de categorias disponíveis na página inicial, filtrando-as com base em uma lista de exclusão. A partir dessas categorias, o programa faz requisições à API do site para coletar informações sobre produtos, como descrição, fabricante e URL das imagens. Ele processa os dados em formato JSON e continua a busca de produtos de forma paginada até que todos os itens de uma categoria sejam extraídos. Por fim, permite a execução automatizada do processo sem configurações adicionais.

#### Como executar a aplicação Extração dos dados da questão 1

##### Executar o programa:
Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose up --build -d extracao_dados_app // este comando irá executar o programa que fará a extração dos dados.

##### acessar os logs da execução do programa em tempo real: 
Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
  
    docker-compose logs -f extracao_dados_app

##### Parar a execução da aplicação:
No diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down



## Questão 2

A solução deve ser implementada utilizando a linguagem Python na versão 3.6+ e a biblioteca usada deve ser Scrapy. O script deve realizar processo de obter o retorno de faturamento do pedido que o usuário der entrada. 

#### Tópicos:
  1. Efetue login no site usando os dados acima;
     
  2. Vá em “Meus Pedidos”;
     
  3. Pesquise o pedido que o usuário inputou nos argumentos do script. Traga o retorno de faturamento no formato json contendo os campos: Motivo, itens [codigo_produto, descricao, quantidade_faturada]. Retorne um erro caso não o encontre o pedido no site.
     

#### Este projeto é um web scraper desenvolvido com a biblioteca Scrapy e integrado ao Playwright para a automação de interações em sites gerados por JavaScript. Ele tem como objetivo acessar o sistema de pedidos eletrônicos da Servimed, realizar login e buscar informações de um pedido específico.

O processo de login é gerenciado pela classe Login, que autentica o usuário e valida o acesso ao sistema. O programa permite a busca de pedidos a partir de um ID fornecido via linha de comando, incluindo informações detalhadas sobre os itens do pedido, como código, descrição e quantidade faturada, utilizando seletores CSS e XPath para localizar elementos específicos na página. Ele também conta com integração ao Playwright, possibilitando o manuseio de páginas dinâmicas e elementos JavaScript, além de gerenciar modais e eventos complexos, como botões de confirmação. Os dados coletados são salvos em formato JSON.

### Dificuldades

  Em Scrapy não foi possível pegar o valor do <input> Motivo dentro do modal detalhes. Retornando NULL em todas as execuções.

#### Como executar a aplicação Extração dos dados da questão 1

##### Executar o programa:
Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:
        
    docker-compose up --build -d extract_pedidos_app
  
##### Depois execute o comando para interagir no container:
Dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando para interagir com o container:

    docker exec -it avaliacao_tecnica_cotefacil-extract_pedidos_app-1 bash

##### Execute o programa de extração de dados no bash do container:
  
    python main.py <código_do_pedio>

##### Parar a execução da aplicação:
  dentro do diretório /Avaliacao_Tecnica_CoteFacil execute o comando no terminal:

    docker-compose down


    
### Adicional da Questão 2

Existe outra aplicação feita em Selenium (Questao_2/Selenium), onde foi possível pegar o Motivo do pedido.

Obs: Deve ser executado no ambiente virtual.


    

## Questão 3

Escreva um script Python que recebe como parâmetro um número n inteiro positivo e imprime no console o n-ésimo valor correspondente da sequência de Fibonacci. Obs.: O problema deve ser resolvido utilizando recursão. 

#### A sequência de Fibonacci é uma série de números naturais em que cada número é a soma dos dois anteriores, começando com 0 e 1. Portanto, a sequência é formada pelos números: 0, 1, 1, 2, 3, 5, 8, 13, 21 e assim por diante. Na terminologia matemática, esta série representa um problema clássico de recursão, uma vez que cada termo da sequência é uma função dos termos precedentes:

F(0) = 0

F(1) = 1

F(2) = F(1) + F(0) 

...

F(n) = F(n-1) + F(n-2) 

#### Programa python para cálculo do n-ésimo termo da série de Fibonacci usando recursão:

### Como executar o programa: ir para o diretório Questao_3

#### Para executar digitar: python fibonacci.py 20

Onde fibonacci.py é o nome do programa python e 20 corresponde à posição do termo na sequência de Fibonacci.


## Questão 4

Explique o problema que poderia acontecer com o programa desenvolvido na questão 1 ao passar como entrada n = 50.


O algoritmo mais simples para cálculo da série de Fibonacci usando recursão se baseia na criação de uma função recursiva que chama quantas vezes forem necessárias até que se atinja o caso base, F(0) ou F(1). O programa fibonacci.py desenvolvido na questão 4 é um exemplo desse algoritmo. Desta forma, problemas menores mas idênticos, são executados de forma repetida, tornando a computação mais pesada conforme n fica maior (complexidade na ordem de 2^n). O tempo de execução cresce exponencialmente porque a função calcula muitos subprocessos idênticos repetidamente. Quando passamos o valor 50 como parâmetro, o script demora muito tempo para executar ou até nem executa, dependendo da capacidade da máquina.

Uma forma de tornar o algoritmo recursivo mais eficiente é armazenando os resultados de chamadas anteriores em uma variável do tipo lista. Dessa forma, quando uma mesma entrada ocorre novamente, basta procurar o resultado correspondente no vetor e retorná-lo, sem precisar executar novamente, reduzindo a complexidade do tempo de execução de O(2^n) para O(n). O programa fibonacci2.py foi implementado com essa otimização.

### Como executar o programa: ir para o diretório Questao_4

#### Para executar, digitar: python fibonacci2.py 60

Onde fibonacci.py é o nome do programa python e 60 corresponde à posição do termo na sequência de Fibonacci.



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




