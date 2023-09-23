from flask import Flask, render_template, request, redirect, url_for
from validate_data import data_load, data_validate, list_columns
from deidentify import deidentify_data
from clean import drop_data_dictionary, drop_columns, check_missing_values, fill_missing_values, check_outliers
from revalidate_data import data_revalidate, list_columns
import pandas as pd
import os
import glob

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#USER INTERFACE
@app.route('/')
def home():
    # Renders the html page in the templates folder
    return render_template('home.html')

#PIPELINE PART 1: DATA IMPORTATION (UPLOAD)
#create a new upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    #get the uploaded file
    uploaded_file = request.files['file']
    #check if a file was uploaded
    if uploaded_file.filename != '':
        #create the complete path to save the file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        #save the file
        uploaded_file.save(file_path)
        return render_template('uploaded.html')
    return 'No file was uploaded'
    
#PIPELINE PART 2: DATA VALIDATION
@app.route('/validate_data', methods=['POST'])
def validate_data():
    global sheets_dict
    # Load the data
    sheets_dict = data_load(app.config['UPLOAD_FOLDER'])
    
    # Check if data loading was successful
    if isinstance(sheets_dict, str):
        return sheets_dict
    
    # Rename 'participantsNov' to 'participants' if it exists
    if 'participantsNov' in sheets_dict:
        sheets_dict['participants'] = sheets_dict.pop('participantsNov')
    
    # Validate the data
    validation_results = data_validate(sheets_dict)
    
    # List the columns
    column_info = list_columns(sheets_dict)
    
    return render_template('validation_results.html', results=validation_results, columns=column_info)

#PIPELINE PART 3: DATA DE-IDENTIFICATION
@app.route('/deidentify_data', methods=['POST'])
def deidentify_route():
    global sheets_dict  # Assuming sheets_dict is a global variable
    sheets_dict, df_participants = deidentify_data(sheets_dict)
    return render_template('deidentified.html', df_participants=df_participants.to_dict(orient='records'))

#PIPELINE PART 4: DATA CLEANING
@app.route('/clean_data', methods=['POST'])
def clean_data():
    global sheets_dict  # Make sure to use the global sheets_dict variable
    # Drop the data dictionary sheet
    sheets_dict = drop_data_dictionary(sheets_dict)
    # Drop specified columns from the 'participants' and 'affiliations' sheets
    sheets_dict, dropped_info = drop_columns(sheets_dict)
    # Check for missing values in all sheets
    missing_values_info = check_missing_values(sheets_dict)
    # Fill missing values in 'responses' and 'participants' sheets
    sheets_dict = fill_missing_values(sheets_dict)
    # Check for outliers in 'participants' and 'responses' sheets
    outliers_info = check_outliers(sheets_dict)
    # Pass the information to the 'cleaned.html' template
    return render_template('cleaned.html', dropped=dropped_info, missing_values=missing_values_info, outliers=outliers_info)

#PIPELINE PART 5: DATA RE-VALIDATION
@app.route('/revalidate', methods=['POST'])
def revalidate_data():
    global sheets_dict
    revalidation_results = data_revalidate(sheets_dict)
    column_info = list_columns(sheets_dict)
    return render_template('revalidation_results.html', results=revalidation_results, columns=column_info)

#PIPELINE PART 5.1: CLEANED DATA EXPORT
@app.route('/export_data', methods=['POST'])
def export_data():
    global sheets_dict  # Make sure to use the global sheets_dict variable
    # Create an Excel writer object
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Cleaned_Data.xlsx')
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        # Loop through each DataFrame and write it to the Excel file
        for sheet_name, df in sheets_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    return render_template('exported.html')

if __name__ == '__main__':
    app.run(debug=True)