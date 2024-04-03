class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = ''
    MYSQL_USER = ''
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'

config={
    'development' : DevelopmentConfig
}