from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class MaintenanceForm(FlaskForm):
    activate_maintenance = SubmitField('Activar Mantenimiento')
    deactivate_maintenance = SubmitField('Desactivar Mantenimiento')