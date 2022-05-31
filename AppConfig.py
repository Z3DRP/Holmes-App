import pymysql.cursors

class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # need to get the con string to mysql
    conStr = "mysql+pymysql://holmesDev:Holmes123@localhost:3306/holmes"
