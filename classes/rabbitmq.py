import configuration

class RabbitMQ:
    def __init__(self, channel_name):
        self.credentials = pika.PlainCredentials(
            configuration.rabbitmq_user,
            configuration.rabbitmq_pass
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=configuration.rabbitmq_host,
                port=configuration.rabbitmq_port,
                virtual_host='/',
                credentials=self.credentials
            )
        )

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=channel_name)

    def publish(self):
        pass

    def consume(self):
        pass