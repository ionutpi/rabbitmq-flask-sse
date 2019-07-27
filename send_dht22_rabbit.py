
import Adafruit_DHT
import time
import pika

#DHT22 pin definition
sensor = Adafruit_DHT.DHT22
pin = 4

#RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='dht22')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    time.sleep(2)
    message=str(humidity)
    channel.basic_publish(exchange='',
                          routing_key='dht22',
                          body=message)
    print("Sent "+message)
    #connection.close()
