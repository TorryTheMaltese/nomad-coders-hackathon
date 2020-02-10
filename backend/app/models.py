import uuid
import json
from datetime import datetime
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
    __table_name__ = "tbl_user"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(64))
    user_password = db.Column(db.String(94))
    user_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_last_seen = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

