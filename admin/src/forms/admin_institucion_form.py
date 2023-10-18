from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class adminInstitucionForm(FlaskForm):
    administrador = SubmitField ('Asignar Administrador')
    operador = SubmitField ('Asignar Operador')
    dueño = SubmitField ('Asignar Dueño')
    