import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic_1 = "noticias/uis"
topic_2 = "noticias/siu"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

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


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        print("Hola! Adelante podrá actualizar las noticias de esta semana, escoja el/los topic a los que quiere enviar su noticia: \n")
        print(f"1 - para actualizar el topic {topic_1}\n")
        print(f"2 - para actualizar el topic {topic_2}\n")
        print(f"3 - para actualizarlos ambos")
        topic = input("\n")

        msg = input("\nDigite el mensaje que desea enviar: \n")
        # result: [0, 1]
        
        if topic == '1':
            result = client.publish(topic_1, msg)
            status = result[0]
            if status == 0:
                print(f"Send message to topic `{topic_1}`")
            else:
                print(f"Failed to send message to topic {topic_1}")
            msg_count += 1
        elif topic == '2':
            result = client.publish(topic_2, msg)
            status = result[0]
            if status == 0:
                print(f"Send message to topic `{topic_1}`")
            else:
                print(f"Failed to send message to topic {topic_1}")
            msg_count += 1
        elif topic == '3':
            result = client.publish(topic_1, msg)
            result = client.publish(topic_2, msg)
            status = result[0]
            if status == 0:
                print(f"Send message to topics `{topic_1} - {topic_2}`")
            else:
                print(f"Failed to send message to topics")
            msg_count += 1
        else:
            print("Failed to find a topic")
        print("\n")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
