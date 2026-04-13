from classes.rabbitmq import RabbitMQ
from datetime import datetime
import time
import random

rabbitmq = RabbitMQ()
rabbitmq.set_queue_declare('sensors')

for i in range(20):
    payload = {
        "id": i,
        "client_name": "Juan Tzuc",
        "client_enabled": True,
        "value": random.randint(1, 100),
        "created_at": datetime.now().isoformat()
    }

    rabbitmq.publish('', 'sensors', payload)
    time.sleep(0.05)

rabbitmq.close_connection()
