import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import json
import requests
import re

pass_file = json.loads(open('passwords.json').read())
API_KEY = pass_file['api_key']

def spanify(word):
    return "<span>" + word + "</span>"

def getSynonyms(word, spanified=False):
    ''' get synonms for a word from bighugelabs api. 
        return a list of strings of each synonym found '''
    url = "http://words.bighugelabs.com/api/2/{}/{}/".format(API_KEY,word)
    resp_map_dict = {'syn':'synonym',
                     'ant':'antonym',
                     'rel':'related',
                     'sim':'similar',
                     'usr':'user_suggested'}

    r = requests.get(url)
    resp = r.text.split('\n')[:-1]
    for index, row in enumerate(resp):
        splits = row.split('|')
        splits[1] = resp_map_dict[splits[1]]
        if spanified:
            splits[2] = spanify(splits[2])
        resp[index] = ' | '.join(splits)

    if len(resp) < 1:
        resp = ['No results found for this word.']
    return resp


class Paragraph:
    def __init__(self, text):
        self.text = text

    def getWords(self):
        #TODO: fix this, because doesn't gracefully handle apostrophes,
        # also does not keep punctuation... str.split() is probably better.
        word_list = re.sub("[^\w]", " ",  self.text).split()        
        return word_list

    def getLookupWordList(self):
        ''' parse a paragraph and return a list of words to do a lookup on ''' 
        tokens = word_tokenize(self.text)
        pos_tags = pos_tag(tokens)

        # preposition (IN), conjunction coordinating(CC), determiner(DT), adverb (RB),
        # Wh-adverb(WRB), modal auxiliary(MD)
        ignore_pos_tags = ['IN','CC','DT','EX','VBD','WRB','MD']
        #TODO: add back Adverbs? (RB)
        lookup_word_list = []
        # iterate through tags, and grab words to look up 
        
        for tag in pos_tags:
            word = tag[0]
            pos = tag[1]

            if len(word) <= 3:
                continue

            if word == 'very':
                continue #TODO: remove this? and make logic for actually checking word that comes afer very
                very_idx = pos_tags.index(tag)
                next_word_idx = pos_tags.index(tag) + 1
            
            if pos in ignore_pos_tags:
                continue
            
            lookup_word_list.append(word)

        return lookup_word_list