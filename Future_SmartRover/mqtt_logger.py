# Placeholder for MQTT-based sensor/data logging to central server

import paho.mqtt.client as mqtt
import json

def publish_data():
    data = {'location': 'junction_01', 'detections': [{'label': 'person', 'conf': 0.89}]}
    client = mqtt.Client()
    client.connect('broker.hivemq.com', 1883, 60)
    client.publish('smart_rover/logs', json.dumps(data))

publish_data()
