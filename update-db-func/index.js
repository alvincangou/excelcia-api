const { Storage } = require('@google-cloud/storage');
const mysql = require('mysql');

const storage = new Storage();

// Configuration de la connexion à la base de données MySQL sur Google Cloud SQL
const dbConfig = {
    user: 'app',
    password: 'app',
    database: 'karucar',
    socketPath: '/cloudsql/karucar:europe-west9:karucar-db'
};

const connection = mysql.createConnection(dbConfig);

exports.updateCarAvailability = async (event, context) => {
    const file = event.name;

    // Extraire l'ID du nom de fichier
    const match = file.match(/car-(\d+)\.jpg/);
    if (!match) {
        console.error(`Filename ${file} does not match expected pattern.`);
        return;
    }

    const carId = parseInt(match[1], 10);

    // Mettre à jour la base de données
    connection.query(
        'UPDATE car SET available = true, file = ? WHERE id = ?',
        [`car-${carId}.jpg`, carId],
        (error, results) => {
            if (error) {
                console.error('Error updating database:', error);
            } else {
                console.log(`Updated car with ID ${carId} to available.`);
            }
        }
    );
};