#!/usr/bin/env python
"""reducer.py"""

import sys

threshold = 0.005

current_word_pairs = None
current_count = 0
current_total = 0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # print(line)
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    # print(key,value)
    # words
    word_i, word_j = key.split(",")
    word_tuple = (word_i, word_j)
    # count, total_basket
    count, total = value.split(",")
    count, total = int(count), float(total)
    # print(word_i, word_j, count, total)
    # new word pairs
    if current_word_pairs == word_tuple:
        current_count += count
        current_total += total
    else:
        if current_word_pairs:
            # print(current_word_pairs, current_count, current_total)
            if current_count/current_total >= threshold:
                (word_a, word_b) = current_word_pairs
                print "%s,%s\t%s" %(word_a, word_b, current_count)
        current_word_pairs = word_tuple
        current_count = count
        current_total = total

# last one
if current_word_pairs:
    if current_count/current_total >= threshold:
        (word_a, word_b) = current_word_pairs
        print "%s,%s\t%s" %(word_a, word_b, current_count)
