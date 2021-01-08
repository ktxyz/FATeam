from FAT.database import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    def height_in_meters(self):
        return self.height / 100