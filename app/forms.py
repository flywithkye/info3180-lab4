from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    pic = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'PNG or JPG Images only!')
    ])