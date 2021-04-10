import django
import json
import os
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from products.models import Product

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='cms')


def callback(ch, method, properties, body):
    product_id = json.loads(body)
    print(product_id)
    product = Product.objects.get(id=product_id)
    product.product_purchase_count = product.product_purchase_count + 1
    product.save()
    print('product order increase')


channel.basic_consume(
    queue='order', on_message_callback=callback, auto_ack=True)

print('RabbitMQ cms service consumer started')

channel.start_consuming()

channel.close()
