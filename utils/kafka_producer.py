# run this script to produce messages to the Kafka topic 'campaign-test'. Testing purpose only.

from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

data_events = [
    {'event_type': 'data_event', 'data': {'key': '123', 'value': 'data_value_1'}},
    {'event_type': 'data_event', 'data': {'key': '456', 'value': 'data_value_2'}},
    {'event_type': 'key_event', 'data': {'key': '123', 'value': 'data_value_1'}},
    {'event_type': 'key_event', 'data': {'key': '456', 'value': 'incorrect_value'}},
]

for event in data_events:
    producer.send('campaign-test', value=event)
    time.sleep(1)
