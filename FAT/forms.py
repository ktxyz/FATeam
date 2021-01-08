from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MemberForm(FlaskForm):
    profile_picture = FileField(validators=[])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    height = StringField('height', validators=[DataRequired()])
    weight = StringField('width', validators=[DataRequired()])