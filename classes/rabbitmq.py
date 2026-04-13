import configuration
import pika
import json

class RabbitMQ:
    def __init__(self, channel_name):        
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
        self.channel.queue_declare(queue=channel_name)

    def set_channel_name(self, channel_name):
        self.channel_name = channel_name

    def set_routing_key(self, routing_key):
        self.routing_key = routing_key

    def publish(self, payload):
        self.channel.basic_publish(
            exchange='', 
            routing_key=self.routing_key, 
            body=json.dumps(payload)
        )

    def consume(self, callback):
        self.channel.basic_consume(
            queue='sensors',
            on_message_callback=callback,
            auto_ack=False
        )

    def callback(ch, method, properties, body):
        data_received = body.decode()
        print(f"Message body: {data_received}")