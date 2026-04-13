import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("192.168.1.123", 1883, 60)

client.subscribe("test/topic")
client.on_message = on_message

client.loop_forever()