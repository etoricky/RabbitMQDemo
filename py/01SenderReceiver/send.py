#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')
body = str(time.time())
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)
print(" [x] Sent " + body)
connection.close()