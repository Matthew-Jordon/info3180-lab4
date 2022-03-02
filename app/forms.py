from wtforms import *
from flask_wtf import *
from flask_wtf.file import *

class UploadForm(FlaskForm):

    file_upload = FileField('image', [validators.DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only')])
    csrf_token = csrf.CSRFProtect()