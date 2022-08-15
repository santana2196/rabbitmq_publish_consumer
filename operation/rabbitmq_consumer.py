import pika, ast
from .operation_bd import ProcessBD

def callback(ch, method, properties, body):
    body_decode = body.decode("UTF-8")
    my_data = ast.literal_eval(body_decode)
    return_bd = ProcessBD(my_data['ano'], my_data['population'])
    return_bd.insert_db()
    return_bd.fechar_cx_db()

def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='process_file')

    channel.basic_consume(queue='process_file',
                        auto_ack=True,
                        on_message_callback=callback)
                        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


