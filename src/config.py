class Config:
    SECRET_KEY ='P1O9P8I0'

class DevelopmentConfig(Config):
    Debug=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='turnero'

config={'development': DevelopmentConfig}