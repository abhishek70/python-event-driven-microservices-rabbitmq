import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='cms')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
    queue='cms', on_message_callback=callback, auto_ack=True)

print('RabbitMQ cms service consumer started')

channel.start_consuming()

channel.close()
