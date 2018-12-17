'''
times.py
'''

import pandas as pd
import read
#import dateutil
from dateutil.parser import parse

def extract_hour(time_stamp):
    datetime_obj = parse(time_stamp)
    return datetime_obj.hour


def main_program():
    df = read.load_data()
    
    #print(df.columns)
    submission_time = df['submission_time']
    print(submission_time.head(5))
    
    print('\nHours:')
    hours = submission_time.apply(extract_hour)
    print(hours.head(5))
    print(hours.value_counts(dropna=False))


if __name__ == '__main__':
    main_program()