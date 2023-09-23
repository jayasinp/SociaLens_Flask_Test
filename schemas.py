from pandas_schema import Schema, Column
from pandas_schema.validation import IsDtypeValidation
import numpy as np

# Schema for each sheet
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