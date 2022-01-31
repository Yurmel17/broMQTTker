import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic_1 = "noticias/uis"
topic_2 = "noticias/siu"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client):
    
    print("Hola! Adelante podrá obtener la noticia más actualizada de esta semana, escoja el/los topic de su interés: \n")
    print(f"1 - para suscribirse al topic {topic_1}\n")
    print(f"2 - para suscribirse al topic {topic_2}\n")
    print(f"3 - para suscribirse a ambos")
    topic = input("\n")
    
    if topic == '1':
        client.subscribe(topic_1)
    elif topic == '2':
        client.subscribe(topic_2)
    elif topic == '3':
        client.subscribe(topic_1)
        client.subscribe(topic_2)
    else:
        print("Failed to find a topic")
    
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
