from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class AssignmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    due_date = DateTimeField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    max_points = IntegerField('Maximum Points', validators=[DataRequired(), NumberRange(min=0)])

class SubmissionForm(FlaskForm):
    file = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc', 'docx', 'txt'], 'Only documents are allowed!')
    ])
    comments = TextAreaField('Comments')
