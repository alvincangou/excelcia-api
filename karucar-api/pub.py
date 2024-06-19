import os
from google.cloud import pubsub_v1
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

project_id = os.getenv("PROJECT_ID")
topic_id = 'cars'
subscription_id = 'cars-sub'

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(project_id, topic_id)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def publish(url, car_id):
    if url:
        message_data = json.dumps({'file_url':url, 'car_id': car_id}).encode('utf-8')
        future = publisher.publish(topic_path, data=message_data)
        return future.result()