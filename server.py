from flask import Flask, render_template, request
import forms
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = json.loads(open('passwords.json').read())['SECRET_KEY']

@app.route('/', methods=['GET','POST'])
def index():
    form = forms.ParagraphForm()
    return render_template('index.html',form=form)

@app.route('/thesaurize', methods=['GET','POST'])
def thesaurize():
    form = forms.ParagraphForm()
    #TODO fix form validation..
    if request.method == 'POST':
        
        # get the synonyms and do soem stuff here for the paragraph text.
        return render_template('thesaurize.html')

if __name__ == '__main__':
    debug = True
    host = '0.0.0.0'
    port = 8000
    app.run(host=host, debug=debug, port=8000)
