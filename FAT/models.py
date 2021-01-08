from FAT.database import db
from FAT.config import FATConfig


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_pic = db.Column(db.String(128))

    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    def height_in_meters(self):
        return self.height / 100

    def get_image_url(self):
        return f'https://{FATConfig.BLOB_ACCOUNT}.blob.core.windows.net/{FATConfig.BLOB_NAME}/{self.profile_pic}'
