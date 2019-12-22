
from collections import Counter
from random import randrange
from string import punctuation

L = []
for i in range(20):
  L.append(randrange(10))
print(L)
c = Counter(L)
print(c)
print()

common = ["the","and","to","a","of","it","said","i","in","was","you","that", 
    "as","at","on","had","with","all","be","for","not","but","so","this","they","what",
    "is","if","an","or","by","then","them"]
cset = set(common)

fn = "/usr/local/doc/alice.txt"
inf = open(fn,"r")
doc = []
for line in inf:
  if line[0] != "#":
    words = line.split()
    for word in words:
      w = word.lower().strip(punctuation)
      if w != "" and w not in cset:
        doc.append(w)
inf.close()

wordcount = Counter(doc)
for word,count in wordcount.most_common(30):
   print("%20s %4d" % (word,count))

