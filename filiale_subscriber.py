import paho.mqtt.client as mqtt
import json
import sqlite3

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
        client.subscribe("vehicle/position")
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, message):
    position_data = json.loads(message.payload.decode())
    print("Received position data:", position_data)
    insert_position_data(position_data['latitude'], position_data['longitude'])

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def insert_position_data(latitude, longitude):
    conn = sqlite3.connect('vehicle_positions.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, latitude REAL, longitude REAL)')
    cursor.execute('INSERT INTO positions (latitude, longitude) VALUES (?, ?)', (latitude, longitude))
    conn.commit()
    conn.close()

broker_address = "broker.hivemq.com"
broker_port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

try:
    client.connect(broker_address, broker_port)
    client.loop_start()
    input("Press Enter to exit...\n")
finally:
    client.loop_stop()
    client.disconnect()