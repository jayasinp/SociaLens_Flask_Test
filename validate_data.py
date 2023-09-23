from pandas_schema import Schema, Column
from pandas_schema.validation import IsDtypeValidation
from schemas import schemas
import pandas as pd
import numpy as np
import glob
import os

schemas = {
    'affiliations': Schema([
        Column('ID', [IsDtypeValidation(np.number)]), # checks if data type is an int or float
        Column('Title', [IsDtypeValidation('O')]), # checks if data type is a string
        Column('Category', [IsDtypeValidation('O')]),
        Column('Description', [IsDtypeValidation(np.number)]),
        Column('nominationWave', [IsDtypeValidation(np.number)]),
        Column('addtional info 2', [IsDtypeValidation(np.number)]),
        Column('additonal info 1', [IsDtypeValidation(np.number)])
    ]),
    
    'participants': Schema([
        Column('Participant-ID', [IsDtypeValidation(np.number)]),
        Column('Type', [IsDtypeValidation('O')]),
        Column('First-Name', [IsDtypeValidation('O')]),
        Column('Last-Name', [IsDtypeValidation('O')]),
        Column('Email', [IsDtypeValidation('O')]),
        Column('Contact Number', [IsDtypeValidation(np.number)]),
        Column('Perc_Effort', [IsDtypeValidation(np.number)]),
        Column('Attendance', [IsDtypeValidation(np.number)]),
        Column('Perc_Academic', [IsDtypeValidation(np.number)]),
        Column('CompleteYears', [IsDtypeValidation(np.number)]),
        Column('House', [IsDtypeValidation('O')])
    ]),
    
    'responses': Schema([
        Column('survey-instance-id', [IsDtypeValidation(np.number)]),
        Column('Participant-ID', [IsDtypeValidation(np.number)]),
        Column('Status', [IsDtypeValidation('O')]),
        Column('Manbox5_1', [IsDtypeValidation(np.number)]),
        Column('Manbox5_2', [IsDtypeValidation(np.number)]),
        Column('Manbox5_3', [IsDtypeValidation(np.number)]),
        Column('Manbox5_4', [IsDtypeValidation(np.number)]),
        Column('Manbox5_5', [IsDtypeValidation(np.number)]),
        Column('isolated', [IsDtypeValidation(np.number)]),
        Column('WomenDifferent', [IsDtypeValidation(np.number)]),
        Column('Manbox5_overall', [IsDtypeValidation(np.number)]),
        Column('language', [IsDtypeValidation(np.number)]),
        Column('question5', [IsDtypeValidation('O')]),
        Column('Masculinity_contrained', [IsDtypeValidation(np.number)]),
        Column('GrowthMindset', [IsDtypeValidation(np.number)]),
        Column('COVID', [IsDtypeValidation(np.number)]),
        Column('criticises', [IsDtypeValidation(np.number)]),
        Column('MenBetterSTEM', [IsDtypeValidation(np.number)]),
        Column('School_support_engage6', [IsDtypeValidation(np.number)]),
        Column('pwi_wellbeing', [IsDtypeValidation(np.number)]),
        Column('Intelligence1', [IsDtypeValidation(np.number)]),
        Column('Intelligence2', [IsDtypeValidation(np.number)]),
        Column('Soft', [IsDtypeValidation(np.number)]),
        Column('opinion', [IsDtypeValidation(np.number)]),
        Column('Nerds', [IsDtypeValidation(np.number)]),
        Column('School_support_engage', [IsDtypeValidation(np.number)]),
        Column('comfortable', [IsDtypeValidation(np.number)]),
        Column('future', [IsDtypeValidation(np.number)]),
        Column('bullying', [IsDtypeValidation(np.number)]),
        Column('candidate_Perc_Effort', [IsDtypeValidation(np.number)]),
        Column('YourComments', [IsDtypeValidation('O')])
    ]),
    
    'net_0_Friends': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_1_Influential': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_2_Feedback': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_3_MoreTime': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_4_Advice': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_5_Disrespect': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ]),
    
    'net_affiliation_0_SchoolActivit': Schema([
        Column('Source', [IsDtypeValidation(np.number)]),
        Column('Target', [IsDtypeValidation(np.number)])
    ])
    }

# creates a dictionary called sheets_dict which reads the .xlsx file
def data_load(upload_folder):
    # Get list of all .xlsx files in the upload_folder
    list_of_files = glob.glob(os.path.join(upload_folder, '*.xlsx'))
    
    # If no files are found, return an error message
    if not list_of_files:
        return "No files found in the upload folder."
    
    # Sort list of files based on last modification time
    latest_file = max(list_of_files, key=os.path.getctime)
    
    # Load the most recently uploaded .xlsx file into a dictionary of DataFrames
    sheets_dict = pd.read_excel(latest_file, sheet_name=None)
    # Rename 'participantsNov' to 'participants' if it exists
    if 'participantsNov' in sheets_dict:
        sheets_dict['participants'] = sheets_dict.pop('participantsNov')
    
    return sheets_dict

def data_validate(sheets_dict):
    validation_results = {}
    for sheet, df in sheets_dict.items():
        if sheet in schemas:
            errors = schemas[sheet].validate(df)
            if not errors:
                validation_results[sheet] = "Valid"
            else:
                error_messages = [str(error) for error in errors]
                validation_results[sheet] = f"Has errors: {', '.join(error_messages)}"
    return validation_results

def list_columns(sheets_dict):
    column_info = {}
    for sheet, df in sheets_dict.items():
        column_info[sheet] = list(df.columns)
    return column_info
