#!/usr/bin/env python
"""mapper.py"""

import sys
from collections import defaultdict

threshold = 0.0025

word_dict = defaultdict(lambda: 0)
total_baskets = 0
baskets = []

# read the basket and save it and count single items
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words.sort()
    for word in words:
        word_dict[word] += 1
    total_baskets += 1
    baskets.append(words)

# print(baskets[0])
# print(baskets[1])

total_baskets = float(total_baskets)

# print(total_baskets)
# print(len(baskets))
# print(len(word_dict))

# frequent single word finding
frequent_word = []
for key, value in sorted(word_dict.iteritems()):
    if value / total_baskets >= threshold:
        frequent_word.append(key)

# print(frequent_word)

frequent_word_set = set(frequent_word)

# generate possible word pairs
word_pair = set()
frequent_word_len = len(frequent_word)
# print("a", frequent_word_len)
for i in range(frequent_word_len):
    for j in range(i+1,frequent_word_len):
        word_tuple = (frequent_word[i], frequent_word[j])
        word_pair.add(word_tuple)

# print("b", len(word_pair))
# print(word_pair)

# run second pass to count possible word pairs
word_pair_dict = defaultdict(lambda: 0)
for basket in baskets:
    count = len(basket)
    for i in range(count):
        if basket[i] in frequent_word_set:
            for j in range(i+1,count):
                word_i, word_j = basket[i], basket[j]
                word_tuple = (word_i, word_j)
                if word_tuple in word_pair:
                    word_pair_dict[word_tuple] += 1

# print("c", len(word_pair_dict))

# frequent word pair finding
frequent_word_pair = []
for key, value in sorted(word_pair_dict.iteritems()):
    if value / total_baskets >= threshold:
        (word_i, word_j) = key
        frequent_word_pair.append(key)

# print("d", len(frequent_word_pair))

frequent_word_pair_set = set(frequent_word_pair)

# generate possible word triplets (with subset checking)
word_triplets = set()
for i in range(frequent_word_len):
    for j in range(i+1,frequent_word_len):
            if (frequent_word[i], frequent_word[j]) in frequent_word_pair_set:
                for k in range(j+1,frequent_word_len):
                    if (frequent_word[i], frequent_word[k]) in frequent_word_pair_set and (frequent_word[j], frequent_word[k]) in frequent_word_pair_set:
                        word_tri = (frequent_word[i], frequent_word[j], frequent_word[k])
                        word_triplets.add(word_tri)

# print("e", len(word_triplets))

# run third pass to count possible word triplets
word_triplet_dict = defaultdict(lambda: 0)
for basket in baskets:
    count = len(basket)
    for i in range(count):
        if basket[i] in frequent_word_set:
            for j in range(i+1,count):
                if basket[j] in frequent_word_set and (basket[i], basket[j]) in frequent_word_pair_set:
                    for k in range(j+1,count):
                        word_i, word_j, word_k = basket[i], basket[j], basket[k]
                        word_tri = (word_i, word_j, word_k)
                        if word_tri in word_triplets:
                            word_triplet_dict[word_tri] += 1

# frequent word triplet finding
frequent_word_triplet = []
for key, value in word_triplet_dict.iteritems():
    if value / total_baskets >= threshold:
        (word_i, word_j, word_k) = key
        print "%s,%s,%s\t%s" %(word_i,word_j,word_k,value)

