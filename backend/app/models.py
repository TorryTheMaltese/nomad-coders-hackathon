import uuid

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

USERS = [
        {
          "id": uuid.uuid4().hex,
          "email": "test",
          "password": "test",
        },
]
