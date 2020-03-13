import uuid
from app import db
from sqlalchemy.sql import func


BOOKS = [
        {
          "id": uuid.uuid4().hex,
          "title": "King Lear",
          "description": "The Story of King Lear",
          "tag": "tragedy"
        },
        {
          "id": uuid.uuid4().hex,
          "title": "Hamlet",
          "description": "The Tragimall Historie of Hamlet, Prince",
          "tag": "tragedy"
        },
        {
          "id": uuid.uuid4().hex,
          "title": "Romeo and Juliet",
          "description": "The Story of their love",
          "tag": "tragedy"
        },
        {
          "id": uuid.uuid4().hex,
          "title": "All's Well That Ends Well",
          "description": "a play by William Shakespeare",
          "tag": "comedy"
        },
        {
          "id": uuid.uuid4().hex,
          "title": "A Midsummer Night's Dream",
          "description": "a play by William Shakespeare",
          "tag": "comedy"
        },
        {
          "id": uuid.uuid4().hex,
          "title": "Twelfth Night",
          "description": "a play by William Shakespeare",
          "tag": "comedy"
        }
      ]


class USERS(db.Model):
    __tablename__ = "tbl_user"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(64))
    user_password = db.Column(db.String(94))
    user_registered = db.Column(db.DateTime, nullable=False, default=func.now())
    user_last_seen = db.Column(db.DateTime, nullable=False, default=func.now())
    token = db.relationship('TOKEN', backref='user', lazy='dynamic')

    def __init__(self, **kwargs):
        self.user_email = kwargs.get('user_email')
        self.user_name = kwargs.get('user_name')
        self.user_password = kwargs.get('user_password')
        self.user_last_seen = kwargs.get('user_last_seen')

    def __repr__(self):
        return '<USER {}>'.format(self.id)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class TOKEN(db.Model):
    __tablename__ = "tbl_token"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_user.id'))
    token_refresh = db.Column(db.String(200))

    def __init__(self, **kwargs):
        self.token_refresh = kwargs.get("token_refresh")

    def __repr__(self):
        return '<TOKEN {}>'.format(self.user_id)
