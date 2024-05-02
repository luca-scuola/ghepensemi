import paho.mqtt.client as mqtt
import time
import json
import random
import threading

broker_address = "broker.hivemq.com"
broker_port = 1883

def generate_position_data():
    latitude = round(45.1234 + (0.001 * (random.randint(-100, 100))), 6)
    longitude = round(9.5678 + (0.001 * (random.randint(-100, 100))), 6)
    return {"latitude": latitude, "longitude": longitude}

def publish_position_data(client):
    while True:
        position_data = generate_position_data()
        client.publish("vehicle/position", json.dumps(position_data))
        print("Dati di posizione pubblicati:", position_data)
        time.sleep(3)

client = mqtt.Client()
client.connect(broker_address, broker_port)

thread = threading.Thread(target=publish_position_data, args=(client,))
thread.start()

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Script interrotto dall'utente.")