from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
class EmailForm(FlaskForm):
    email = StringField('Email: ', validators=[Email()])
    submit = SubmitField('Ввести')