from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class MaintenanceForm(FlaskForm):
    activate_maintenance = SubmitField('Activar Mantenimiento')
    deactivate_maintenance = SubmitField('Desactivar Mantenimiento')
    
    
class ContactoForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message="Este campo es obligatorio"),
                                    Email(message="El mail ingresado no es válido.")])
    guardar = SubmitField('guardar')