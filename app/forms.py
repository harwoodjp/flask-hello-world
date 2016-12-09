from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class AddPost(Form):
	author = StringField('author', validators=[DataRequired()])
	date = StringField('date', validators=[DataRequired()])	
	title = StringField('title', validators=[DataRequired()])	
	body = StringField('body', widget=TextArea(), validators=[DataRequired()])
