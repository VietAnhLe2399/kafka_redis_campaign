import json

def start_consumer(consumer, redis_client):
    print("Consumer started!")
    for message in consumer:
        event = message.value
        event_type = event.get('event_type')
        event_data = event.get('data')
        print(f"Received event: {event}")

        if event_type == 'key_event':
            redis_data = redis_client.get(event_data['key'])
            if redis_data:
                redis_data = json.loads(redis_data)
                if redis_data == event_data:
                    print(f"Match found: {redis_data}")
                else:
                    print(f"Data mismatch: Redis: {redis_data}, Kafka: {event_data}")
            else:
                print(f"No data found in Redis for key: {event_data['key']}")
        else:
            redis_client.set(event_data['key'], json.dumps(event_data))
