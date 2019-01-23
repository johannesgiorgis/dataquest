'''
exploration.py
'''

import pandas as pd

def print_value_counts(data, column_name):
    print("\n{0} Column Value Counts:".format(column_name))
    print(data[column_name].value_counts(dropna=False))
    
    
def main_program():
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    
    print_value_counts(data, "JJ")
    print_value_counts(data, "SCH_STATUS_MAGNET")
    
    # count number of students in juvenile justice facilities
    
    pivot_table_jj = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], 
                                    index="JJ", aggfunc='sum')
    print("\nJJ Pivot Table:\n", pivot_table_jj)
    
    # count number of students in magnet schools
    pivot_table_ms = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], 
                                    index="SCH_STATUS_MAGNET", aggfunc='sum')
    print("\nMS Pivot Table:\n", pivot_table_ms)
    
    
if __name__ == "__main__":
    main_program()