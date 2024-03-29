#!/usr/bin/env python

import sys
from mr import emit


def count_vowels(line):
    """
    A map function that counts the vowels in a line.
    """
    for vowel in 'aeiou':
        count = line.count(vowel)
        if count > 0:
            emit(vowel, count)


for line in sys.stdin:
    count_vowels(line)
