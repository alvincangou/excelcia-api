from flask import send_file
from . import main
from google.cloud import storage

client = storage.Client()
BUCKET_NAME = 'karu-image'


@main.route('/files/car/<int:id>', methods=['GET'])
def get_car_file(id):
    IMAGE_NAME = f'car-{id}.jpg'
    try:
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(IMAGE_NAME)

        # Télécharge le contenu de l'image dans un fichier temporaire
        temp_image = '/tmp/temp_image.jpg'  # Chemin temporaire pour sauvegarder l'image
        blob.download_to_filename(temp_image)

        # Renvoie le fichier image en réponse
        return send_file(temp_image, mimetype='image/jpeg')

    except Exception as e:
        return str(e), 500