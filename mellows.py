from marshmallow import fields, Schema
import datetime as dt

class TitleCased(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return ''
        return value.title()


class UserSchema(Schema):
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    # titlename = TitleCased(attribute="name")
    titlename = TitleCased()
    since_created = fields.Method("get_days_since_created")


    def get_days_since_created(self, obj):
        return dt.datetime.now().day - obj.created_at.day