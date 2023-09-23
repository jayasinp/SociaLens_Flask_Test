import math
from scipy import stats
import numpy as np

def drop_data_dictionary(sheets_dict):
    sheets_dict.pop('data_dictionary', None)
    return sheets_dict

def drop_columns(sheets_dict):
    dropped_info = {}
    if 'affiliations' in sheets_dict:
        cols_to_drop = ['Description', 'nominationWave', 'addtional info 2', 'additonal info 1']
        sheets_dict['affiliations'].drop(cols_to_drop, axis=1, inplace=True)
        dropped_info['affiliations'] = cols_to_drop
    return sheets_dict, dropped_info

def check_missing_values(sheets_dict):
    missing_values_info = {}
    for sheet, df in sheets_dict.items():
        missing_values = df.isna().sum()
        missing_values_info[sheet] = missing_values
    return missing_values_info

def fill_missing_values(sheets_dict):
    if 'responses' in sheets_dict:
        sheets_dict['responses'].drop(['question5'], axis=1, inplace=True)
        columns_to_fill = [
            'Manbox5_1', 'Manbox5_2', 'Manbox5_3', 'Manbox5_4', 'Manbox5_5',
            'isolated', 'WomenDifferent', 'Manbox5_overall', 'language', 
            'Masculinity_contrained', 'GrowthMindset', 'COVID', 'criticises', 
            'MenBetterSTEM', 'School_support_engage6', 'pwi_wellbeing', 
            'Intelligence1', 'Intelligence2', 'Soft', 'opinion', 'Nerds', 
            'School_support_engage', 'comfortable', 'future', 'bullying'
        ]
        for col in columns_to_fill:
            median_value = sheets_dict['responses'][col].median()
            rounded_up_median = math.ceil(median_value)
            sheets_dict['responses'][col].fillna(rounded_up_median, inplace=True)
    
    if 'participants' in sheets_dict:
        median_value = sheets_dict['participants']['Perc_Academic'].median()
        sheets_dict['participants']['Perc_Academic'].fillna(median_value, inplace=True)
    return sheets_dict

def check_outliers(sheets_dict):
    outliers_info = {}
    if 'participants' in sheets_dict:
        cols_to_check_participants = ['Perc_Effort', 'Attendance', 'Perc_Academic', 'CompleteYears']
        outliers_info['participants'] = {}
        for col in cols_to_check_participants:
            if col in sheets_dict['participants'].columns:  # Check if the column exists
                z_scores = np.abs(stats.zscore(sheets_dict['participants'][col]))
                outliers = np.where(z_scores > 3)
                outliers_info['participants'][col] = len(outliers[0])
    
    if 'responses' in sheets_dict:
        cols_to_check_responses = ['candidate_Perc_Effort']
        outliers_info['responses'] = {}
        for col in cols_to_check_responses:
            if col in sheets_dict['responses'].columns:  # Check if the column exists
                z_scores = np.abs(stats.zscore(sheets_dict['responses'][col]))
                outliers = np.where(z_scores > 3)
                outliers_info['responses'][col] = len(outliers[0])
    return outliers_info