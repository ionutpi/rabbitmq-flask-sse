# -*- coding: utf-8 -*-
from flask import Flask, Response,render_template
import random
import time
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='dht22')

app = Flask(__name__)

def event_stream():
    for method_frame, properties, body in channel.consume('dht22'):

        # Display the message parts
        print body

        # Acknowledge the message
        channel.basic_ack(method_frame.delivery_tag)
        yield 'data: %s\n\n' % body


@app.route('/')
def root():
    return render_template('index5.html')

@app.route('/stream')
def stream():
    return Response(event_stream(),
                          mimetype="text/event-stream")


if __name__ == '__main__':
    #app.debug = True
    app.run(threaded=True,host='0.0.0.0')
