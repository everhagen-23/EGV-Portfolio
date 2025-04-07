import nltk
import nltk.corpus
nltk.download('book')
from nltk.book import *
from urllib import request
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext
import io
import sys

words = ["whale", "sea", "ship", "captain"]
nltk.draw.dispersion_plot(text1, words)
plt.show

bookurl= "https://www.gutenberg.org/cache/epub/2081/pg2081.txt"
response = request.urlopen(bookurl)
br = response.read().decode('utf8')
type(br)
print(len(br))
howLong = len(br)
print(f"howLong = {howLong}")
novelSlice = br[:500]
print(f"novelSlice = {novelSlice}")

splitEmUp = br.split()
print(f"splitEmUp = {splitEmUp[-100:]}")

for token in splitEmUp:
    if token.endswith('ing'):
        print(token)

        from nltk.corpus import inaugural
inaugural.fileids()
cfd = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    if fileid[:4] > "1990"
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()
plt.show()

f = open('C:/Users/spook/Music/_my-repos/DIGIT210-PokemonMoves/docs/support/gen1.txt')
raw = f.read()
bookurl= "file:///C:/Users/spook/Music/_my-repos/DIGIT210-PokemonMoves/docs/support/gen1.txt"
response = request.urlopen(bookurl)
br = response.read().decode('utf8')
type(br)
print(len(br))
howLong = len(br)
print(f"howLong = {howLong}")
novelSlice = br[:500]
print(f"novelSlice = {novelSlice}")

splitEmUp = br.split()
print(f"splitEmUp = {splitEmUp[-100:]}")

 # unsure how to get the graphing plots working here
for token in splitEmUp:
    if token.endswith('ing'):
            print(token)
                nltk.draw.dispersion_plot

for token in splitEmUp:
    if token.endswith('ing'):
            print(token)
splitEmUp.draw.dispersion_plot
