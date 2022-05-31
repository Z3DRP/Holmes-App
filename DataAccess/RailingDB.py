from app import Railing, db
from sqlalchemy import update

class RailingDB:
    @staticmethod
    def GetRailings():
        try:
            railings = Railing.query.order_by(Railing.name).all()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
        return railings

    @staticmethod
    def GetRailing(rid):
        try:
            railing = Railing.query.get(rid)
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
        return railing

    @staticmethod
    def AddRailing(productcode, name, railtype, price, image):
        try:
            railing = Railing(productcode, name, railtype, price, image)
            db.session.add(railing)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

    @staticmethod
    def UpdateRailing(rid, productcode, name, railtype, price, image):
        try:
            rowsAffected = update('Railings').where(
                Railing.id == rid).values(
                {
                    "Product_Code": productcode,
                    "Name": name,
                    "Rail_Type": railtype,
                    "Price_Per_SqFt": price,
                    "Image": image
                })
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

        if not rowsAffected > 0:
            return False
        else:
            return True

    @staticmethod
    def DeleteRailing(rid):
        try:
            db.session.delete(Railing).where(Railing.id == rid)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
