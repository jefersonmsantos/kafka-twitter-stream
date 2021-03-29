## Twitter Stream using Python, Kafka and MongoDB
Este aplicativo é um modelo simplificado de extração real time de tweets e posterior persistência em uma base de dados do Mongo DB.

A aplicação se utiliza da solução Apache Kafka para realizar o streaming dos tweets coletados pelo crawler desenvolvido em python que monitora os tweets contendo uma palavra determinada, a cada intervalo de tempo determinado.

Após, as mensagens disponibilizadas no tópico do Kafka são consumidas e armazenadas em uma base de dados do Mongo DB.

Para acessar o API do Twitter, é necessário criar uma conta de desenvolvedor no Twitter e obter as chaves de acesso.

## Como realizar o deploy da aplicação
1. Copie os arquivos deste repositório para o local em que deseja executar o aplicativo;
2. Crie um arquivo .env e defina as seguintes variáveis de ambiente para acessar sua conta do twitter e sua conta do Mongo DB:
    * API_Key
    * API_Secret_key
    * access_token 
    * access_token_secret

    * mongopath 
    * mongouser 
    * password 

3. Abra um terminal de comando e execute o comando "docker-compose up -d" para iniciar a instância do Kafka
4. Abra um novo terminal de comando, e inicie o producer do kafka, executando o comando "python stream_tweet.py"
5. Abra um novo terminal de comando, e inicie o consumer do kafka, executando o comando "python consume_tweet.py
6. Para visualizar o tópico do kafka e as mensagens, acesse através do browser o caminho "localhost:19000"
7. As mensagens devem estar sendo armazenados em sua base do MongoDB
8. Para alterar os termos a serem pesquisados, altere o valor da string argumento da função api.search(), no arquivo stream_tweet.py 


## License and Author info
MIT License

Copyright (c) 2021 Jeferson Machado Santos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.