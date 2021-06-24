import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import json 

import models, database


models.Base.metadata.create_all(database.engine)
db = database.SessionLocal()

json_file = open("util/db_data.json", "r")
data = json.load(json_file)

items = data['positions']
for item in items:
    position = models.Position(
        id               = item.get('id'),
        component_number = item.get('component_number'),
        section_number   = item.get('section_number'),
        name             = item.get('name'),
        description      = item.get('description')
    )
    db.merge(position)

items = data['english_text']
for item in items:
    english_text = models.EnglishText(
        id      = item.get('id'),
        position_id = item.get('position_id'),
        text    = item.get('text')
    )
    db.merge(english_text)

items = data['korean_text']
for item in items:
    english_text = models.KoreanText(
        id      = item.get('id'),
        position_id = item.get('position_id'),
        text    = item.get('text')
    )
    db.merge(english_text)

items = data['images']
for item in items:
    image = models.Image(
        id          = item.get('id'),
        position_id = item.get('position_id'),
        directory   = item.get('directory')
    )
    db.merge(image)

items = data['memberships']
for item in items:
    membership = models.Membership(
        id    = item.get('id'),
        name  = item.get('name'),
        price = item.get('price')
    )
    db.merge(membership)

items = data['status']
for item in items:
    status = models.Status(
        id   = item.get('id'),
        name = item.get('name')
    )
    db.merge(status)

json_file.close()

db.commit()
db.close()
