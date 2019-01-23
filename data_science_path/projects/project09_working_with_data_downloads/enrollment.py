'''
enrollment.py
'''

import pandas as pd
import pprint
    
def main_program():
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    
    # total enrollment
    all_enrollment = data['total_enrollment'].sum()
    print('\nAll Enrollment:', all_enrollment)
    
    # school enrollment statistics
    school_enr_stats = {
        'SCH_ENR_HI_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_HI_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_AM_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_AM_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_AS_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_AS_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_HP_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_HP_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_BL_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_BL_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_WH_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_WH_F': {'sum': 0, 'percent': 0},
        'SCH_ENR_TR_M': {'sum': 0, 'percent': 0},
        'SCH_ENR_TR_F': {'sum': 0, 'percent': 0},
    }
    
    for col in school_enr_stats.keys():
        school_enr_stats[col]['sum'] = data[col].sum()
    
    # calculate percentage of enrollment for each race and gender
    for col in school_enr_stats.keys():
        school_enr_stats[col]['percent'] = school_enr_stats[col]['sum'] / all_enrollment
    
    # summary
    print('\nSchool Enrollment Stats:')
    pprint.pprint(school_enr_stats)
    
    
if __name__ == "__main__":
    main_program()