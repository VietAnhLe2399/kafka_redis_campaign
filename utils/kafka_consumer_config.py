from kafka import KafkaConsumer
from utils.constant_variables import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, KAFKA_GROUP_ID
import json

class KafkaConsumerConfig:
    def __init__(self, topic=KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_GROUP_ID):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id

    def create_consumer(self):
        return KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=self.group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
