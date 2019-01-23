'''
domains.py
'''

import pandas as pd
import numpy as np
import read


def extract_last_url_word(url):
    #print(url)
    return url.split('.')[-1]


def extract_last_two_url_words(url):
    url_list = url.split('.')
    #print(url, len(url_list))
    if len(url_list) > 1 and url_list[-1] != 'com':
        return '.'.join(url_list[-2:])
    return ''


def extract_last_n_url_words(url):
    url_list = url.split('.')
    
    if len(url_list) > 2:
        return '.'.join(url_list)
    return ''

    
def remove_com_subdomains(url):
    url_list = url.split('.')
    domain_types = ['com', 'org', 'gov', 'edu',
                   'it', 'io', 'de', 'ch', 'es',
                   'in', 'se', 'ca', 'net', 'tv'
                   'fm', 'name', 'me', 'fr', 'nl' ]
    if url_list[-1] in domain_types and len(url_list) > 2:
        return '.'.join(url_list[-2:])
    else:
        return url


def main_program():
    df = read.load_data()
    
    print(df.columns)
    
    print(df.head(5))
    
    domains = df['url'].value_counts(dropna=False)
    print(domains)
    
    #for name, row in domains.items():
    #    print("{0}: {1}".format(name, row))
    
    # remove nan values from url series
    urls = df['url'].dropna()
    
    print(urls.value_counts(dropna=False))
    
    #last_url_word = urls.apply(extract_last_url_word)
    
    #print('\nLast URL Word:')
    #print(set(last_url_word))
    
    #last_two_url_words = urls.apply(extract_last_two_url_words)
    
    #print('\nLast 2 URL Words:')
    #print(set(last_two_url_words))
    
    print('\nRemove Subdomains:')
    clean_urls = urls.apply(remove_com_subdomains)
    
    print(set(clean_urls))
    print(type(clean_urls), len(clean_urls))
    
    #print('\nLast URL Word:')
    #last_two_url_words = clean_urls.apply(extract_last_two_url_words)
    #print(set(last_two_url_words), len(set(last_two_url_words)))
    
    print('\nLast URL Word:')
    last_n_url_words = clean_urls.apply(extract_last_n_url_words)
    print(set(last_n_url_words), len(set(last_n_url_words)))
    
    '''
    need to differentiate domains like bbc.co.uk 
    '''


if __name__ == '__main__':
    main_program()