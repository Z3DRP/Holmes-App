from app import Design, db
from sqlalchemy import update

class DesignDB:
    @staticmethod
    def GetDesigns():
        try:
            designs = Design.query.order_by(Design.customer_id)
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
        return designs

    @staticmethod
    def GetDesign(did):
        try:
            design = Design.query.get(did)
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
        return design

    @staticmethod
    def AddDesign(customerID, deckID, railID, len, width, sqft, start):
        try:
            design = Design(customerID, deckID, railID, len, width,sqft,start)
            db.session.add(design)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

    @staticmethod
    def UpdateDesign(did, customerID, deckID, railID, len, width, sqft, start):
        try:
            rowsAffected = update('Designs').where(
                Design.id == did).values(
                {
                    "Customer_Id": customerID,
                    "Deck_Id": deckID,
                    "Rail_Id": railID,
                    "Length": len,
                    "Width": width,
                    "Square_Ft": sqft,
                    "Start_Date": start
                })
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")
        if not rowsAffected > 0:
            return False
        else:
            return True

    @staticmethod
    def DeleteDesign(did):
        try:
            db.session.delete(Design).where(Design.id == did)
            db.session.commit()
        except ConnectionError:
            raise Exception("An error occurred while connecting to database")

