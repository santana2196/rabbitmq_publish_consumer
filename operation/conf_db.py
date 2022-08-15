import os

sql ='''CREATE TABLE if not exists population (
            id INTEGER PRIMARY KEY,
            ano INT,
            population INT,
            date text
)'''

caminho_do_bd = os.path.abspath('./operation/banco/db.sqlite3')