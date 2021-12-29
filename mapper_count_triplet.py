#!/usr/bin/env python
"""mapper.py"""

import sys

frequency_word_triplets = set()
word_triplet_dict = {}

with open("word_triplets") as f:
    for line in f.readlines():
        line = line.strip()
        word_i, word_j, word_k = line.split(",")
        word_tri = (word_i, word_j, word_k)
        frequency_word_triplets.add(word_tri)
        word_triplet_dict[word_tri] = 0

total_baskets = 0

# run second pass and count frequent word triplets
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words.sort()
    count = len(words)
    for i in range(count):
        for j in range(i+1,count):
            for k in range(j+1,count):
                word_i, word_j, word_k = words[i], words[j], words[k]
                word_tri = (word_i, word_j, word_k)
                if word_tri in frequency_word_triplets:
                    word_triplet_dict[word_tri] += 1
    total_baskets += 1

# output to the reducer
for key, value in word_triplet_dict.iteritems():
    (word_i, word_j, word_k) = key
    print "%s,%s,%s\t%s,%s" %(word_i, word_j, word_k, value, total_baskets)