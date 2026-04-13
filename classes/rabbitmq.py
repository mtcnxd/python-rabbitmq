import configuration
import pika
import json

class RabbitMQ:
    def __init__(self):
        credentials = pika.PlainCredentials(
            configuration.rabbitmq_user,
            configuration.rabbitmq_pass
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=configuration.rabbitmq_host,
                port=configuration.rabbitmq_port,
                virtual_host='/',
                credentials=credentials
            )
        )

        self.channel = self.connection.channel()

    def set_queue_declare(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish(self, exchange, routing_key, payload):
        self.channel.basic_publish(
            exchange=exchange, 
            routing_key=routing_key, 
            body=json.dumps(payload)
        )
        print(f"Message body: {payload}")

    def consume(self, callback, auto_ack=False):
        self.channel.basic_consume(
            queue='sensors',
            on_message_callback=callback,
            auto_ack=auto_ack
        )

    def callback(self, ch, method, properties, body):
        data_received = body.decode()
        print(f"Internal body: {data_received}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()