from nltk.corpus import wordnet as wn
import random
sent = input("Enter the Sentence\n")
words_syn = {}
for i in sent.split():
  possible_words = wn.synsets(i)
  if possible_words:
    words_syn[i]=possible_words[0].lemma_names()
re_sen={}
for i,j in words_syn.items():
   words_syn[i] = random.choice(j)
rewritten = sent.split()
for i,j in enumerate(rewritten):
  if j in words_syn:
  rewritten[i]=words_syn[j]
result = " ".join(rewritten)
print(result)
