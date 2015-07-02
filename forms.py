from flask.ext.wtf import Form
from wtforms.fields import TextField
#from wtforms.validators import Required, Length
from wtforms import validators
class ParagraphForm(Form):
    paragraph_text = TextField('paragraph_text', [validators.Required(), validators.Length(max=400)])

