from app import Decking, db
from sqlalchemy import update

# add method for pagenation of decking for selection on web page

class DeckingDB:
    @staticmethod
    def GetDeckings():
        try:
            decking = Decking.query.order_by(Decking.name).all()
        except ConnectionError:
            raise Exception("An error occurred while retrieving data")
        return decking

    @staticmethod
    def GetDecking(did):
        try:
            decking = Decking.query.get(did)
        except ConnectionError:
            raise Exception("An error occured while retrieving data")

        return decking

    @staticmethod
    def AddDecking(productcode, name, decktype, price, image):
        try:
            deck = Decking(productcode, name, decktype, price, image)
            db.session.Add(deck)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occured while retrieving data")

    @staticmethod
    def UpdateDecking(did, productcode, name, decktype, price, image):
        try:
            rowsAffected = update('Deckings').where(
                Decking.id == did).values(
                {
                    "Product_Code": productcode,
                    "Name": name,
                    "Deck_Type": decktype,
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
    def DeleteDecking(did):
        try:
            db.session.delete(Decking).where(Decking.id == did)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")


