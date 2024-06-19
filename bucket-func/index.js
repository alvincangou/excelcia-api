const { Storage } = require('@google-cloud/storage');
const axios = require('axios');
const { PubSub } = require('@google-cloud/pubsub');
const pubsub = new PubSub();

const storage = new Storage();
const bucketName = 'karu-image';

exports.downloadFile = async (message, context) => {
    const pubsubMessage = message.data
        ? Buffer.from(message.data, 'base64').toString()
        : null;

    if (pubsubMessage) {
        try {
            const { file_url, car_id } = JSON.parse(pubsubMessage);

            // Téléchargement du fichier depuis l'URL
            const response = await axios({
                url: file_url,
                method: 'GET',
                responseType: 'stream',
            });

            // Envoi du fichier téléchargé dans le bucket
            const destinationFile = storage.bucket(bucketName).file(`car-${car_id}.jpg`);
            const writeStream = destinationFile.createWriteStream({
                resumable: false,
            });

            response.data.pipe(writeStream);

            await new Promise((resolve, reject) => {
                writeStream.on('finish', resolve);
                writeStream.on('error', reject);
            });

            console.log(`File downloaded and uploaded to ${car_id}.jpg in bucket ${bucketName}`);
        } catch (error) {
            console.error('Error downloading or uploading file:', error);
            throw new Error('File download/upload failed');
        }
    } else {
        console.log('No data received in the message');
    }
};