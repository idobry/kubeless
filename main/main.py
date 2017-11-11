import logging
from flask import Response, Flask
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError

consumer = KafkaConsumer(bootstrap_servers = 'kafka:9092')
consumer.subscribe(topics=['toScreen'])

application = Flask(__name__)

@application.route('/')
def index():
    return "Hello World!"


@application.route('/stream')
def kafkaStream():
    return Response(events(), mimetype='text/plain')
    

def events():
    try:            
        for message in consumer:
            if message is not None:
                yield (message.value + '\n')
    except KafkaError as e:
            logging.info("**ERROR**"+str(e))
    

if __name__ == '__main__':
    application.run(debug = True, host='0.0.0.0')

