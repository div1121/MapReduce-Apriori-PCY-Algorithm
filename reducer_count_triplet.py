#!/usr/bin/env python
"""reducer.py"""

import sys

threshold = 0.0025

current_word_triplets = None
current_count = 0
current_total = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    # words
    word_i, word_j, word_k = key.split(",")
    word_tri = (word_i, word_j, word_k)
    # count, total_basket
    count, total = value.split(",")
    count, total = int(count), float(total)

    # new word pairs
    if current_word_triplets == word_tri:
        current_count += count
        current_total += total
    else:
        if current_word_triplets:
            if current_count/current_total >= threshold:
                (word_a, word_b, word_c) = current_word_triplets
                print "%s,%s,%s\t%s" %(word_a, word_b, word_c, current_count)
        current_word_triplets = word_tri
        current_count = count
        current_total = total

# last one
if current_word_triplets:
    if current_count/current_total >= threshold:
        (word_a, word_b, word_c) = current_word_triplets
        print "%s,%s,%s\t%s" %(word_a, word_b, word_c, current_count)
