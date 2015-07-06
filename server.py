from flask import Flask, render_template, request, url_for
import forms
import json
import thesaurize
import os

app = Flask(__name__)
APP_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SECRET_KEY'] = json.loads(open(APP_DIR+'/passwords.json').read())['SECRET_KEY']

@app.route('/', methods=['GET','POST'])
def index():
    form = forms.ParagraphForm()
    return render_template('index.html',form=form)

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    
    form = forms.ParagraphForm()
    #TODO fix form validation..
    if request.method == 'POST':
        print form
        submitted_text = request.form['paragraph_text']
        #TODO: fix vtemplate validation.
        if len(submitted_text) <= 0:
            return render_template('index.html', form=form)
        paragraph = thesaurize.Paragraph(submitted_text)
        
            
        orig_span_list = ' '.join([thesaurize.spanify(w) for w in submitted_text.split()])
        lookup_word_list = paragraph.getLookupWordList()

        # iterate through the lookup words and create a list of dict-lists
        final_word_map_list = []
        for word in lookup_word_list:
            synonym_dict = {}
            print "checking synonyms for word {}".format(word)
            synonym_dict[word] = thesaurize.getSynonyms(word,spanified=True)
            final_word_map_list.append(synonym_dict)
        # get the synonyms and do soem stuff here for the paragraph text.
        return render_template('thesaurize.html', 
                                submitted_text=submitted_text,
                                orig_span_list=orig_span_list,
                                lookup_word_list=lookup_word_list,
                                final_word_map_list=final_word_map_list)



if __name__ == '__main__':
    debug = True
    host = '0.0.0.0'
    port = 8000
    app.run(host=host, debug=debug, port=8000)
