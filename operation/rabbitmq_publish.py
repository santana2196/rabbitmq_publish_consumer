import pika

def process_rabbitmq(message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='process_file')
	channel.basic_publish(exchange='',
						  routing_key='process_file',
						  body=str(message))

	connection.close()