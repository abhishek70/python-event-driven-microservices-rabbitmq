import pika, json

from app import Product, db

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='order')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    print(properties)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['product_title'], image=data['product_image'])
        db.session.add(product)
        db.session.commit()
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['product_title']
        product.image = data['product_image']
        db.session.commit()
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('RabbitMQ order service consumer started')

channel.start_consuming()

channel.close()
