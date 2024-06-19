import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://user1:user1@/'
        f'karu-db?unix_socket=/cloudsql/vincent-exelcia:europe-west9:formation-db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False