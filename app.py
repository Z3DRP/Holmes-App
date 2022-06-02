from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from AppConfig import DevConfig
from flask_bootstrap import Bootstrap
from flask import render_template
from DataAccess import DeckingDB as d
from DataAccess import RailingDB as r
from DataAccess import CustomerDB as c
from DataAccess import DesignDB as da


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
boostrap = Bootstrap(app)


class Customer(db.Model):
    __tablename__ = 'Customers'

    id = db.column(db.Integer(), primary_key=True)
    first_name = db.column(db.String(100), nullable=False, index=True)
    last_name = db.column(db.String(100), nullable=False, index=True)
    email = db.column(db.String(100), nullable=False)
    phone_number = db.column(db.CHAR(12), nullable=False)
    street_address = db.Column(db.String(75), nullable=False,)
    city = db.Column(db.String(75), nullable=False, index=True)
    state = db.column(db.String(50), nullable=False, index=True)
    zipcode = db.column(db.CHAR(5), nullable=False)

    def __init__(self, firstname, lastname, email, phone, street, city,
                 state, zipcode):
        self._fname = firstname
        self._lname = lastname
        self._email = email
        self._phone = phone
        self._street = street
        self._city = city
        self._state = state
        self._zip = zipcode

    def __repr__(self):
        return "<Customer '{}' '{}'>".format(self._fname, self._lname)

    def GetFullname(self):
        return self._fname + " " + self._lname


class Decking(db.Model):
    __tablename__ = 'Deckings'

    id = db.column(db.Integer(), primary_key=True)
    product_code = db.column(db.String(255), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    deck_type = db.column(db.String(100), nullable=False, index=True)
    price_per_sqFt = db.Column(db.DECIMAL, nullable=False, index=True)
    image = db.column(db.String(255), nullable=False, index=True)

    def __init__(self, productcode, name, decktype, price, image):
        self._prodCode = productcode
        self._name = name
        self._decktype = decktype
        self._price = price
        self._image = image


    def __repr__(self):
        return "<Decking '{}' '{}'>".format(self._prodCode, self._name)


class Railing(db.Model):
    __tablename__ = 'Railings'

    id = db.column(db.Integer(), primary_key=True)
    product_code = db.column(db.String(255), nullable=False, index=True)
    name = db.column(db.String(255), nullable=False, index=True)
    rail_type = db.column(db.String(100), nullable=False, index=True)
    price_per_sqFt = db.Column(db.DECIMAL, nullable=False)
    image = db.column(db.String(255), nullable=False, index=True)

    def __init__(self, productcode, name, railtype, price, image):
        self._prodCode = productcode
        self._name = name
        self._railtype = railtype
        self._price = price
        self._image = image


    def __repr__(self):
        return "<Railing '{}' '{}'>".format(self._prodCode, self._name)

    # need to create a currency format func
    def FormatPrice(self):
        pass

class Design(db.Model):
    __tablename__ = 'Designs'

    id = db.column(db.Integer(), primary_key=True)
    customer_id = db.relationship('Customer', backref='Design', lazy='dynamic')
    decking_id = db.relationship('Decking', backref='Design', lazy='dynamic')
    railing_id = db.relationship('Railing', backref='Design', lazy='dynamic')
    length = db.column(db.DECIMAL, nullable=False)
    width = db.column(db.DECIMAL, nullable=False)
    square_ft = db.column(db.DECIMAL, nullable=False)
    start_date = db.column(db.DateTime, nullable=False)
    estimate = db.column(db.DECIMAL, nullable=False, index=True)

    def __init__(self, customerid, deckid, railid, len, width, sqft, start, est):
        self._custmrId = customerid
        self._deckId = deckid
        self._railId = railid
        self._length = len
        self._width = width
        self._sqFt = sqft
        self.start_date = start
        self._estimate = est

    def __repr(self):
        return "<Design '{}' '{}' '{}'>".format(self._custmrId, self._deckId,
                                                self._railId)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/get-decking')
def GetDecking():
    decks = Decking.query.order_by(Decking.name.desc())
    return render_template('GetDecking.html', decks=decks)


@app.route('/get-deck/<int:id>')
def GetDeck(id):
    if not id > 0:
        decks = Decking.query.order_by(Decking.name.desc())
        return render_template('GetDecking.html', decks=decks)
    else:
        deck = d.DeckingDB.GetDecking(id)
        return render_template('GetDeck.html', deck=deck)


@app.route('/get-railing')
def GetRailing():
    rails = Railing.query.order_by(Railing.name.desc())
    return render_template('GetRailing.html', rails=rails)


@app.route('/get-railing/<int:id>')
def GetRail(id):
    if not id > 0:
        rail = Railing.query.order_by(Railing.name.desc())
        return render_template('GetRailing.html', rails=rail)
    else:
        rail = r.RailingDB.GetRailing(id)
        return render_template('GetRail.html', rail=rail)


@app.route('/get-customer')
def GetCustomers():
    customers = Customer.query.order_by(Customer.last_name.desc())
    return render_template('GetCustomers.html', customers=customers)


@app.route('/get-customer/<int:id>')
def GetCustomer(id):
    if not id > 0:
        customers = Customer.query.order_by(Customer.last_name.desc())
        return render_template('GetCustomers.html', customers=customers)
    else:
        customer = c.CustomerDB.GetCustomer(id)
        return render_template('GetCustomer.html', customer=customer)


@app.route('/get-designs')
def GetDesigns():
    designs = Design.query.order_by(Design.start_date.desc())
    return render_template('GetDesigns.html', designs=designs)


@app.route('/get-designs/<int:id>')
def GetDesign(id):
    if not id > 0:
        design = Design.query.order_by(Design.start_date.desc())
        return render_template('GetDesigns.html', designs=design)
    else:
        design = da.DesignDB.GetDesign(id)
        return render_template('GetDesign.html', design=design)


if __name__ == '__main__':
    app.run()
