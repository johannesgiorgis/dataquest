'''
read.py
'''

import pandas as pd

def main_program():
    contents = pd.read_csv("dataCRDC2013_14content.csv")
    print(contents.head(5))
    
    print("Columns: {0}".format(contents.columns))
    

if __name__ == "__main__":
    main_program()