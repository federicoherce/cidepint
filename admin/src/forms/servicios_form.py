from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired

class ServiciosForm(FlaskForm):
    nombre = StringField('Nombre del Servicio', validators=[DataRequired()])
    descripcion = StringField('Descripción del Servicio', validators=[DataRequired()])
    keywords = StringField('Palabras Claves', validators=[DataRequired()])
    centros = StringField('Centros Habilitados', validators=[DataRequired()])
    tipo_servicio = SelectField('Tipo de Servicio', choices=[
        ('Análisis', 'Análisis'),
        ('Consultoría', 'Consultoría'),
        ('Desarrollo', 'Desarrollo')
    ], validators=[DataRequired()])
    habilitado = BooleanField('Habilitado', default=True)