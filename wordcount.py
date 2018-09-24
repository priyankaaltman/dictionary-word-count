# put your code here.
import sys
from collections import Counter

def word_counter(file):
    the_file = open(file)

    exclude = ['?', ",", "(", ")", "'"]  

    word_counts = {}
    for line in the_file:
        words = line.split()  # ['word', 'here']

        for word in words:
            word = word.lower()

            new_word = "".join((char for char in word if char not in exclude))

            word_counts[new_word] = word_counts.get(new_word, 0) + 1



    for new_word, count in word_counts.items():
        print (new_word, count)

word_counter("test.txt")


word_counter(sys.argv[1])
