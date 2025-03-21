import pika, sys, os, logging
from datetime import datetime


logger = logging.getLogger(__name__)

def logit(message):
    timeString = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    logger.info(timeString + " - [mq-rcvr] - " + message)

def main():
    queue_name = os.environ.get('QUEUE', "[QUEUE NOT SET]")
    rmq_host = os.environ.get('RMQ_HOST', "[HOST NOT SET")

    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f"Received {body}")
        logit(f"Received {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
