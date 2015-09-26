from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length


class RegisterUserForm(Form):
    name = StringField('Your name', validators=[Required(), Length(1, 255)])
    submit = SubmitField('Submit')


class EditUserForm(Form):
    name = StringField('Your name', validators=[Required(), Length(1, 255)])
    submit = SubmitField('Submit')
