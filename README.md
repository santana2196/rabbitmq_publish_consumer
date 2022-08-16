<h1>Projeto</h1>

<p>Enfilera o arquivo no rabbitmq e consome enviando os dados para sqlite<p>

<p2>Maos Obra</p2>

<h1> 
<img src= https://media.giphy.com/media/l9Jhzwdi09Ve0/giphy.gif width="300px"/> 
</h1>
 

<h2>Lib pika</h2>

pip install pika

<h2>subir docker compose</h2>

docker-compose up -d

<h2>usuario do rabbitmq</h2>
guest:guest

<h2>publicar na fila</h2>

python3 publish_rabbitmq.py 

<h2>Consumir</h2>

python3 consumer-rabbitmq.py

<h2>consultar no sqlite</h2>

sqlite3 operation/banco/db.sqlite3

sqlite> select count(*) from population;
