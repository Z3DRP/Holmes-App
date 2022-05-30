from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from AppConfig import DevConfig
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
boostrap = Bootstrap(app)


class Customer(db.Model):
    id = db.column(db.Integer(), primary_key=True)
    first_name = db.column(db.String(100), nullable=False, index=True)
    last_name = db.column(db.String(100), nullable=False, index=True)
    email = db.column(db.String(100), nullable=False)
    phone_number = db.column(db.CHAR(12), nullable=False)
    street_address = db.Column(db.String(75), nullable=False,)
    city = db.Column(db.String(75), nullable=False, index=True)
    state = db.column(db.String(50), nullable=False, index=True)
    zipcode = db.column(db.CHAR(5), nullable=False)

    def __init__(self, firstname, lastname):
        self._fname = firstname
        self._lname = lastname

    def __repr__(self):
        return "<Customer '{}' '{}'>".format(self._fname,self._lname)


class Decking(db.Model):
    id = db.column(db.Integer(), primary_key=True)
    product_code = db.column(db.String(255), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    deck_type = db.column(db.String(100), nullable=False, index=True)
    price_per_sqFt = db.Column(db.DECIMAL, nullable=False, index=True)
    image = db.column(db.String(255), nullable=False, index=True)

    def __init__(self, productcode, name):
        self._prodCode = productcode
        self._name = name

    def __repr__(self):
        return "<Decking '{}' '{}'>".format(self._prodCode, self._name)


class Railing(db.Model):
    id = db.column(db.Integer(), primary_key=True)
    product_code = db.column(db.String(255), nullable=False, index=True)
    name = db.column(db.String(255), nullable=False, index=True)
    rail_type = db.column(db.String(100), nullable=False, index=True)
    price_per_sqFt = db.Column(db.DECIMAL, nullable=False)
    image = db.column(db.String(255), nullable=False, index=True)

    def __init__(self, productcode, name):
        self._prodCode = productcode
        self._name = name

    def __repr__(self):
        return "<Railing '{}' '{}'>".format(self._prodCode, self._name)


class Design(db.Model):
    id = db.column(db.Integer(), primary_key=True)
    customer_id = db.relationship('Customer', backref='Design', lazy='dynamic')
    decking_id = db.relationship('Decking', backref='Design', lazy='dynamic')
    railing_id = db.relationship('Railing', backref='Design', lazy='dynamic')
    length = db.column(db.DECIMAL, nullable=False)
    width = db.column(db.DECIMAL, nullable=False)
    square_ft = db.column(db.DECIMAL, nullable=False)
    start_date = db.column(db.DateTime, nullable=False)

    def __init__(self, customerId, deckId, railId):
        self._custmrId = customerId
        self._deckId = deckId
        self._railId = railId

    def __repr(self):
        return "<Design '{}' '{}' '{}'>".format(self._custmrId, self._deckId,
                                                self._railId)


@app.route('/')
def home():  # put application's code here
    return '<h1>Holmes Restoration</h1>'


if __name__ == '__main__':
    app.run()
