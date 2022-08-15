
from csv import DictReader
from .rabbitmq_publish import process_rabbitmq

def function_process_file(file):
    return_processado = []
    with open(file, encoding='utf-8-sig') as arquivo:
        leitor_csv = DictReader(arquivo, delimiter=';')
        for i in leitor_csv:
            return_processado.append(i)
    to_queue(return_processado)
    return print('processado', len(return_processado))

def to_queue(dados):
    for id, i in enumerate(dados):
        C = 'C' + str(id)
        C = {"id": C , "ano": i['ano'], 'population': i['population']}
        process_rabbitmq(C)