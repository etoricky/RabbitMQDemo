#!/usr/bin/env python
import pika
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    # if forget basic_ack, server accumulates messages
    # when client quits, server resends to other consumers
    # sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()