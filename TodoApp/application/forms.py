from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class ItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=30)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=2, max=300)])
    completed = SelectField("Completed", choices=[("False", "False"), ("True", "True")], validators=[DataRequired()])
    submit = SubmitField("Add Item")


