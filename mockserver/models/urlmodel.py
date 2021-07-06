from db import db

class UrlModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80))
    url = db.Column(db.String(200))

    def __init__(self, key, url):
        self.key = key
        self.url = url

    def json(self):
        return {'id':self.id, 'key': self.key, 'url': self.url}

    @classmethod
    def find_by_key(cls, key):
        return cls.query.filter_by(key=key).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()