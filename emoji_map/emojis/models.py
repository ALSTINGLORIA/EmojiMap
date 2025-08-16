from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

class EmojiSubmission(Document):
    emoji = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'indexes': [
            {'fields': ['created_at']},
            {'fields': ['latitude', 'longitude']}
        ]
    }
