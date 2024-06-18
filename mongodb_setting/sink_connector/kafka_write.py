from kafka import KafkaProducer
import json
from json import dumps

p = KafkaProducer(bootstrap_servers = ['kafka2:29093','kafka3:29094'], value_serializer = lambda x:dumps(x).encode('utf-8'))

data = {'name': 'roscoe'}

p.send('shopify2.pets', value = data)

p.flush()