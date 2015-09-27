from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import Required, Length

from app.models import User


class RegisterUserForm(Form):
    name = StringField('Your name', validators=[Required(), Length(1, 255)])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        user = User.query.filter_by(name=field.data).first()
        if user:
            raise ValidationError('Username already in use.')


class EditUserForm(Form):
    name = StringField('Your name', validators=[Required(), Length(1, 255)])
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_name(self, field):
        if not self.user:
            raise ValidationError('Invalid User.')

        user = User.query.filter_by(name=field.data).first()
        if user and user.name != self.user.name:
            raise ValidationError('Username already in use.')
