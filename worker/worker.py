import time
import random
from kafka import KafkaProducer
from kafka.errors import KafkaError

MAX_MSG = 10

def run(context):
    try:
        count = 0
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        while count < MAX_MSG:
            count+=1
            producer.send('kubeless', context + '_' + str(count))       
            time.sleep(1)
    except KafkaError as e:
           print("**ERROR**"+str(e))
    
    producer.close()


