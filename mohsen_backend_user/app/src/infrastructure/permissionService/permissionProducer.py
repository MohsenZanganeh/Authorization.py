from kafka import KafkaProducer
from flask import json
import os
import config
import ast
KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_SERVER = ast.literal_eval(KAFKA_SERVER)
class permission_Produceres:
    def __init__(self) -> None:
        pass
    def __init__(self):
        print(KAFKA_SERVER)
        print(type(KAFKA_SERVER))
        self.producer = KafkaProducer(
        bootstrap_servers = KAFKA_SERVER,
        value_serializer = lambda m: json.dumps(m).encode('ascii'))
        
    
    def register_permission(self, value):
        TOPIC_NAME = config.TOPICS['user']
        producer = self.producer.send(TOPIC_NAME,{'key':'register_permission','value':value})
        producer.add_callback(self._on_send_success).add_errback(self._on_send_error)
        
    def flush_close(self):
        self.producer.flush()
        self.producer.close()
    
    def _on_send_success(self,record_metadata):
        print(f"""
        ------SECCUSS------
        Topic: {record_metadata.topic}
        Partition: {record_metadata.partition}
        Offset: {record_metadata.offset}

        """)
 
    def _on_send_error(self,excp):
        print(f""" 
        ------ERROR------
        {excp}
        """)
