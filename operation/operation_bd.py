import sqlite3
from .conf_db import sql, caminho_do_bd

class ProcessBD:
    def __init__(self, ano, population):
        self.ano = ano
        self.population = population
        self.bd = caminho_do_bd
        self.conn = sqlite3.connect(self.bd)
        self.cursor = self.conn.cursor()
    
    def acessar_db(self):
        self.conn = sqlite3.connect(self.bd)
        self.cursor = self.conn.cursor()
        return self.conn, self.cursor

    def fechar_cx_db(self):
        self.cursor.close()

    def insert_db(self):
        self.cursor.execute(f'''INSERT INTO population(ano, population, date) VALUES ({self.ano}, {self.population}, datetime('now'))''')
        self.conn.commit()
        self.cursor.close()

    def create_db(self):
        try:
            self.cursor.execute('''select * from population''')
            db_teste = str(input('Ja existe tabela, quer recriar: Y/N '))
            if db_teste == 'Y':
                self.cursor.execute("DROP TABLE IF EXISTS population")
                self.cursor.execute(sql)
                print("Table created successfully........")
                self.conn.commit()
            elif db_teste == 'N': 
                print('Nao deseja recriar tabela')
                pass
            else:
                print('Nao digitou a letra correta')
            
            self.fechar_cx_db()

        except:
            print('Nao existe tabela')
            self.cursor.execute(sql)
            self.conn.commit()
            self.fechar_cx_db()

    def query(self):
        self.acessar_db()
        self.cursor.execute('''select * from population''')
        result = self.cursor.fetchall();
        print(result)
        self.conn.commit()
        self.fechar_cx_db()








