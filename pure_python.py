import redis

from utils.constant_variables import REDIS_HOST, REDIS_PORT, REDIS_DB
from utils.kafka_consumer_config import KafkaConsumerConfig
from utils.kafka_consumer_utils import start_consumer

# this can be moved to a separate file like utils/kafla_consumer.py
# create a Redis client
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# initialize Kafka consumer
kafka_config = KafkaConsumerConfig()
consumer = kafka_config.create_consumer()

if __name__ == '__main__':
    start_consumer(consumer, redis_client)
