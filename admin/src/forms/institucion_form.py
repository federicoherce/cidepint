from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class InstitucionForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    informacion = StringField('Informacion', validators=[DataRequired(), Length(max=255)])
    direccion = StringField('Direccion', validators=[Length(max=50)])
    localizacion = StringField('Localizacion', validators=[Length(max=100)])
    palabras_claves = StringField('Palabras Claves', validators=[DataRequired(), Length(max=50)])
    horarios = StringField('Horarios', validators=[Length(max=50)])
    web = StringField('Web', validators=[Length(max=50)])
    contacto = StringField('Contacto', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Agregar')
    
