import sys
import io
import random
from collections import Counter

def main(book_url, n):
    """ """
    text = reader(book_url)
    dict = dicts(text)
    writer(dict, n)

def reader(book_url):
    """ """
    f = io.open(book_url, "r")
    book_string = f.read()
    f.close()

    input_list = book_string.split()

    return input_list

def dicts(input_list):
    """ Reads text and builds dictionaries based on words """

    dict = {'the the': ['the']}

    for i in range(len(input_list) - 2):
        if input_list[i] + ' ' + input_list[i+1] not in dict:
            dict[input_list[i] + ' ' + input_list[i+1]] = [input_list[i+2]]
        else:
            dict[input_list[i] + ' ' + input_list[i+1]].append([input_list[i+2]])      
    return dict

def writer(dict, n):
    dict_keys = list(dict.keys())
    passage = []
    words = random.choice(dict_keys)
    passage.append(words)
    print(passage)
    for i in range(n):
        if words in dict:
            word = random.choice( dict[ words ])
            if isinstance(word, list):
                word = word[ 0 ]
            passage.append( word )
            l = words.split()
            words = l[1] + ' ' + word

    passage = ' '.join(passage)
    print(passage)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
