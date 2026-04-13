from classes.rabbitmq import RabbitMQ
from datetime import datetime
from json import loads

def callback(ch, method, properties, body):
    data_received = body.decode()
    json_data = loads(data_received)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(json_data)

rabbitmq = RabbitMQ()
rabbitmq.set_queue_declare('sensors')

rabbitmq.consume(callback)

rabbitmq.start_consuming()
rabbitmq.close_connection()
