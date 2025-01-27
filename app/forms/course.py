from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    start_date = DateTimeField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateTimeField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
