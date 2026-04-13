from datetime import datetime
import configuration
import pika
import time
import random
import json

# Parámetros de conexión
credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=configuration.rabbitmq_host,
        port=configuration.rabbitmq_port,
        virtual_host='/',
        credentials=credentials
    )
)

channel = connection.channel()

# Declare a queue to ensure it exists
channel.queue_declare(queue='sensors')

# Publish a message

for i in range(500):
    message = {
        "id": i,
        "client_name" : "Marcos Tzuc",
        "client_status": "enabled",
        "value": random.randint(1, 100),
        "created_at": datetime.now().isoformat()
    }
        
    channel.basic_publish(
        exchange='amq.topic', 
        routing_key='sensors.*', 
        body=json.dumps(message)
    )
    
    print(f"Sent data {i}")
    time.sleep(0.5)

connection.close()
