import pika
import time
import json

credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.1.123',
        credentials=credentials
    )
)

channel = connection.channel()

channel.queue_declare(queue='sensors')

def callback(ch, method, properties, body):
    data_received = body.decode()

    print(f"Message body: {data_received}")

    json_data = json.loads(data_received)

    # print(f"Mensaje id: {json_data['id']} with value: {json_data['value']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    time.sleep(0.2)

channel.basic_consume(
    queue='sensors',
    on_message_callback=callback,
    auto_ack=False
)

print('Esperando mensajes...')
channel.start_consuming()