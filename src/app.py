#!/usr/bin/env python
import pika, sys, os

def main():
    queue_name = os.environ.get('QUEUE', "hello")
    rmq_host = os.environ.get('RMQ_HOST', "[HOST NOT SET")

    
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_host))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

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
