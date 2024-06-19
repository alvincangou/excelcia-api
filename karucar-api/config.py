import os

class Config:
    #SQLALCHEMY_DATABASE_URI = (
    #    f'mysql+pymysql://user1:user1@/'
    #    f'karu-db?unix_socket=/cloudsql/vincent-exelcia:europe-west9:formation-db'
    #)
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@/'
        f'{os.getenv("DB_NAME")}?unix_socket=/cloudsql/{os.getenv("CLOUD_SQL_CONNECTION_NAME")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False