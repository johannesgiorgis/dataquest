'''
count.py
'''

import pandas as pd
import read
import collections


def combine_headlines_into_str(df):
    # combine all headlines into 1 string
    print('\nHeadlines:')
    headlines = df['headline'].tolist()
    print(type(headlines), len(headlines))
    print(headlines[:5])
    
    print('\nHeadlines as 1 string:')
    headlines_str = ' '.join(str(headline) for headline in headlines)
    print(type(headlines_str), len(headlines_str))
    
    #print('\nNon-String Headlines:')
    #non_str = headline if isinstance(headline, str) for headline in headlines
    #print(len(non_str))
    
    return headlines_str
    
    
def count_words(words):
    print('Counting words...')
    # lowercase words
    lowercase_words = []
    for word in words:
        #print(type(word))
        lowercase_words.append(word.lower())

    return collections.Counter(lowercase_words)
    

def main_program():
    df = read.load_data()
    
    print(df.head(5))
    
    headlines_str = combine_headlines_into_str(df)
    
    # split headlines_str to list of words
    print('\nWords:')
    words = headlines_str.split(' ')
    print(type(words), len(words))
    
    word_count = count_words(words)
    print(type(word_count))
    
    print('\n100 Most Common Words:')
    print(word_count.most_common(100))


if __name__ == '__main__':
    main_program()