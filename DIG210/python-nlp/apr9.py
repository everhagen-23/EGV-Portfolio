import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import urllib.request
from nltk.corpus import wordnet as wn

filepath = 'C:/Users/spook/Music/_my-repos/DIGIT210-PokemonMoves/pokemonMoves.xml'
f = open(filepath, 'r', encoding='utf8').read()
tokenList = word_tokenize(f)
lowercaseTokens = [token.lower() for token in tokenList]
uniqueTokens = set(lowercaseTokens)
POStagged = pos_tag(uniqueTokens)

#categories to gather
verb = ['VB', 'VBZ']
noun = ['NNS','NN','NNP','NNPS',]
adjective = ['JJR','JJS']
mtype = ['fire','water','grass','psychic','fairy','ground','rock','dark','fighting','steel','normal','bug','electric','dragon','flying','ghost','ice','poison',]
adverb = ['RB','RBR','RBS']
conj = ['IN',]


shortListV = [word for word, tag in POStagged if tag in verb]
shortListN = [word for word, tag in POStagged if tag in noun]
shortListA = [word for word, tag in POStagged if tag in adjective]
shortListT = [word for word, tag in POStagged if tag in mtype]
shortListD = [word for word, tag in POStagged if tag in adverb]
shortListC = [word for word, tag in POStagged if tag in conj]

#add -> count, percentage(?)
#generally not super accurate as list goes on
print('VERBS LIST:')
#sorting out verbs
for w in sorted(shortListV):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")

print('NOUN LIST:')
#sorting out nouns
for w in sorted(shortListN):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")

print('ADJECTIVE LIST:')
#adjectives list
for w in sorted(shortListA):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")

print('ADVERB LIST:')
#sorting out adverbs
for w in sorted(shortListD):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")

print('CONJUCTION LIST:')
#sorting out conjuctions
for w in sorted(shortListC):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")

print('TYPE LIST:')
#sorting out type names - not working rn
for w in sorted(shortListT):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w

    print(f"Word: {w} | Wordnet Lemma: {lemma}")