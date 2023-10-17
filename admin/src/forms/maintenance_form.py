from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class MaintenanceForm(FlaskForm):
    activate_maintenance = SubmitField('Activar Mantenimiento')
    deactivate_maintenance = SubmitField('Desactivar Mantenimiento')
    mensaje = StringField('Mensaje')
    guardar = SubmitField('guardar mensaje')
    
    
class ContactoForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message="Este campo es obligatorio"),
                                    Email(message="El mail ingresado no es válido.")])
    telefono = StringField('Telefono', validators=[DataRequired(message="Este campo es obligatorio")])
    direccion = StringField('Direccion', validators=[DataRequired(message="Este campo es obligatorio")])
    
    guardar = SubmitField('guardar')
    
class paginadoForm(FlaskForm):
    per_page = IntegerField('cantidad de elementos por pagina', validators=[DataRequired(message="Este campo es obligatorio")])
    guardar = SubmitField('guardar')
    
    
    
    
    
    