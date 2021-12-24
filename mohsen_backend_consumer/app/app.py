from kafka import KafkaConsumer
from flask import json
from event_handler.index import event_handler
import os
from flask import current_app as app
import config
import ast
KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_SERVER = ast.literal_eval(KAFKA_SERVER)
print(f'------------------------------------KAFKA_SERVER-{KAFKA_SERVER}--------------------------')
consumer = KafkaConsumer(bootstrap_servers = KAFKA_SERVER,
value_deserializer=lambda m: json.loads(m.decode('ascii')),
group_id='mohsen',
auto_offset_reset='earliest')
# you want read from very very beginning of your topic
# auto_offset_reset='latest')  only the new messages on the boards

consumer.subscribe((config.TOPICS['user'],config.TOPICS['fs'],config.TOPICS['user']))

try:

    for message in consumer:
        Value = message.value.get('value')
        Key = message.value.get('key')

        print(f"""
            Value: {Value}
            Key: {Key}
            Offset: {message.offset}
            topic: {message.topic}
            partition: {message.partition}
        """)
        
        event_handler(message.topic,key=Key,value=Value)
except Exception as err:
    print(err)
    


