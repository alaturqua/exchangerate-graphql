from api import db


class ExchangeRate(db.Model):

    __tablename__ = "exchangerate"

    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.String)
    rate = db.Column(db.Float)
    currency_code = db.Column(db.String)
    date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "base": self.base,
            "rate": self.rate,
            "currency_code": self.currency_code,
            "date": self.date
        }
