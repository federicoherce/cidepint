from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class adminInstitucionForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message="Este campo es obligatorio"),
                                    Email(message="El mail ingresado no es válido.")])
