## Twitter Stream using Python, Kafka and MongoDB
Este aplicativo é um modelo simplificado de extração real time de tweets e posterior persistência em uma base de dados do Mongo DB.

A aplicação se utiliza da solução Apache Kafka para realizar o streaming dos tweets coletados pelo crawler desenvolvido em python que monitora os tweets contendo uma palavra determinada, a cada intervalo de tempo determinado.

Após, as mensagens disponibilizadas no tópico do Kafka são consumidas e armazenadas em uma base de dados do Mongo DB.

Para acessar o API do Twitter, é necessário criar uma conta de desenvolvedor no Twitter e obter as chaves de acesso.

## Como realizar o deploy da aplicação
1 - Copie os arquivos deste repositório para o local em que deseja executar o aplicativo;
2 - Crie um arquivo .env e defina as seguintes variáveis de ambiente para acessar sua conta do twitter e sua conta do Mongo DB:
    - API_Key
    - API_Secret_key
    - access_token 
    - access_token_secret

    - mongopath 
    - mongouser 
    - password 

3 - Abra um terminal de comando e execute o comando "docker-compose up -d" para iniciar a instância do Kafka
4 - Abra um novo terminal de comando, e inicie o producer do kafka, executando o comando "python stream_tweet.py"
5 - Abra um novo terminal de comando, e inicie o consumer do kafka, executando o comando "python consume_tweet.py
6 - Para visualizar o tópico do kafka e as mensagens, acesse através do browser o caminho "localhost:19000"
7 - As mensagens devem estar sendo armazenados em sua base do MongoDB
8 - Para alterar os termos a serem pesquisados, altere o valor da string argumento da função api.search(), no arquivo stream_tweet.py 


## License and Author info