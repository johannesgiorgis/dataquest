'''
read.py
'''

import pandas as pd


def load_data():
    # no header row - add column names
    column_names = ['submission_time', 'upvotes', 'url', 'headline']
    df = pd.read_csv("hn_stories.csv",
                    names = column_names)
    return df


def main_program():
    df = load_data()
    print(df.head(5))
    

if __name__ == '__main__':
    main_program()
