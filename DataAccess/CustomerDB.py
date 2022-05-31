from app import Customer, db
from sqlalchemy import update

class CustomerDB:
    @staticmethod
    def GetCustomers():
        try:
            customers = Customer.query.order_by(Customer.last_name).all()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

        return customers

    @staticmethod
    def GetCustomer(cid):
        try:
            customer = Customer.query.get(cid)
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

        return customer

    @staticmethod
    def FindCustomer(firstname, lastname):
        try:
            customer = Customer.query.where(
                Customer.first_name.ilike(firstname),
                Customer.last_name.ilike(lastname))
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

        return customer

    @staticmethod
    def AddCustomer(fname, lname, email, phone, street, city, state, zipcode):
        customer = Customer(fname, lname, email, phone,
                            street, city, state, zipcode)
        db.session.add(customer)
        db.session.commit()

    @staticmethod
    def UpdateCustomer(id, fname, lname, email, phone, street, city,
                       state, zipcode):
        try:
           rowsAffected = update('Customers').where(
               'Customers.Id' == id).values(
               {"First_Name": fname,
                "Last_Name": lname,
                "Email": email,
                "Phone_Number": phone,
                "Street_Address": street,
                "City": city,
                "State": state,
                "Zipcode": zipcode})
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

        if not rowsAffected > 0:
            return False
        if rowsAffected > 0:
            return True


    @staticmethod
    def DeleteCustomer(cid):
        try:
            db.session.delete(Customer).where(Customer.id == cid)
            db.session.commit()
        except ConnectionError:
            raise Exception("There was an error connection to database")












