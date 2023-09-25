from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(),  Email()])
    submit = SubmitField('Registrar')
    
    
class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')
