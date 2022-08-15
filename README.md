<h1 align="center">Projeto</h1>

Enfilera o arquivo no rabbitmq e consome enviando os dados para sqlite 

#lib pika

pip install pika

#subir docker compose

docker-compose up -d

#usuario do rabbitmq

guest:guest

#publicar na fila

python3 publish_rabbitmq.py 

#Consumir

python3 consumer-rabbitmq.py

#consultar no sqlite

sqlite3 operation/banco/db.sqlite3
sqlite> select count(*) from population;
