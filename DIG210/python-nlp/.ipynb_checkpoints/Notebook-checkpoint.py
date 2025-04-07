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
plt.show()