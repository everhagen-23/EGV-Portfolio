from nltk.corpus import PlaintextCorpusReader
corpus_root = 'C:/Users/spook/Music/_my-repos/DIGIT210-PokemonMoves/docs/support'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

def lexical_diversity(text):    return print(len(set(text)) / len(text))
def percentage(count, total):    return print(100 * count / total)

lexical_diversity('gen1.txt')
lexical_diversity('gen2.txt')

len('gen1.txt')
len('gen2.txt')

sorted(set('gen1.txt'))
sorted(set('2.txt'))





