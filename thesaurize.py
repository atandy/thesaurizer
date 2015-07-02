import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import json
import requests

pass_file = json.loads(open('passwords.json').read())
API_KEY = pass_file['api_key']

def getSynonyms(word):
    url = "http://words.bighugelabs.com/api/2/{}/{}/".format(API_KEY,word)
    r = requests.get(url)
    resp = r.text.split('\n')
    return resp


def parseParagraph(paragraph):
     
    tokens = word_tokenize(paragraph)
    pos_tags = pos_tag(tokens)
    
    # preposition, conjunction coordinating, determiner, adverb
    ignore_pos_tags = ['IN','CC','DT','EX','VBD']
    #TODO: add back Adverbs? (RB)
    lookup_word_list = []
    # iterate through tags, and grab words to look up 
    
    for tag in pos_tags:
        word = tag[0]
        pos = tag[1]

        if len(word) <= 2:
            continue

        if word == 'very':
            continue #TODO: remove this? and amke logic for actually checking word that comes afer very
            very_idx = pos_tags.index(tag)
            next_word_idx = pos_tags.index(tag) + 1
            '''
            if pos_tags[next_word_idx][1] in ignore_pos_tags:
                tag = tag + ('do_lookup',)
                print tag
            '''
        
        tag = tag + ('do_lookup',)

        if pos in ignore_pos_tags:
            continue
        print tag
    return pos_tags
    
paragraph = "There were four people over there, all sitting very quietly."


get_syn_word = parseParagraph(paragraph)



print "checking synonyms for word {}".format(get_syn_word)
synonyms = getSynonyms(get_syn_word)

print synonyms

