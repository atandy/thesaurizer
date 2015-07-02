import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import json
import requests

pass_file = json.loads(open('passwords.json').read())
API_KEY = pass_file['api_key']

def getSynonyms(word):
    ''' get synonms for a word from bighugelabs api. 
        return a list of strings of each synonym found '''
    url = "http://words.bighugelabs.com/api/2/{}/{}/".format(API_KEY,word)
    r = requests.get(url)
    resp = r.text.split('\n')
    return resp


def parseParagraph(paragraph):
    ''' parse a paragraph and return a list of words to do a lookup on ''' 
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
        
        if pos in ignore_pos_tags:
            continue
        
        lookup_word_list.append(word)

    return lookup_word_list


paragraph = "There were four people over there, all sitting very quietly."
lookup_word_list = parseParagraph(paragraph)

# iterate through the lookup words and create a list of dict-lists
final_word_map_list = []
for word in lookup_word_list:
    synonym_dict = {}
    print "checking synonyms for word {}".format(word)
    synonym_dict[word] = getSynonyms(word)
    final_word_map_list.append(synonym_dict)

print final_word_map_list
