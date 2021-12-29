#!/usr/bin/env python
"""mapper.py"""

import sys

# check set
frequency_word_pairs = set()
# counting
word_pair_dict = {}

with open("word_pairs") as f:
    for line in f.readlines():
        line = line.strip()
        word_i, word_j = line.split(",")
        word_tuple = (word_i, word_j)
        # print(word_tuple)
        frequency_word_pairs.add(word_tuple)
        word_pair_dict[word_tuple] = 0

# total baskets        
total_baskets = 0

# run second pass and count frequent word pairs
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words.sort()
    count = len(words)
    for i in range(count):
        for j in range(i+1,count):
            word_i, word_j = words[i], words[j]
            word_tuple = (word_i, word_j)
            if word_tuple in frequency_word_pairs:
                word_pair_dict[word_tuple] += 1
    total_baskets += 1

# output to the reducer
for key, value in word_pair_dict.iteritems():
    (word_i, word_j) = key
    print "%s,%s\t%s,%s" %(word_i, word_j, value, total_baskets)