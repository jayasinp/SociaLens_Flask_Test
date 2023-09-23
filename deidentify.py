import hashlib

def hash_value(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

def deidentify_data(sheets_dict):
    if 'participants' in sheets_dict:
        df_participants = sheets_dict['participants']
        for column in ['First-Name', 'Last-Name', 'Email']:
            df_participants[column] = df_participants[column].apply(hash_value)
        df_participants.drop('Contact Number', axis=1, inplace=True)
        sheets_dict['participants'] = df_participants
        return sheets_dict, df_participants
    else:
        return sheets_dict, None

# problem is re-identification
