import json

# kafka config
KAFKA_TOPIC = 'campaign-test'
KAFKA_HOST = 'localhost'
KAFA_PORT = 9092
KAFKA_GROUP_ID='group-id'
KAFKA_BOOTSTRAP_SERVERS = f'{KAFKA_HOST}:{KAFA_PORT}'

# redis config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0