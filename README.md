# SociaLens_Flask_Test
My work on the backend for SociaLens in Python and Flask


# SociaLens Flask Test
This is a test of the backend functions of SociaLens using a Flask app to handle movement of data between the front-end and back-end.

## Installation
1. First download the files from the github repository.

2. Open up the folder in VSCode

3. Now create a python virtual environment with this code in terminal:
```bash
python3 -m venv venv
```

4. A venv folder will appear in your root directory. We will now install several python packages to run the code.
```bash
pip install scipy numpy hashlib pandas pandas_schema networkx
```
This will install the necessary python libraries into your virtual environment

## Running the application
1. in terminal type in
```bash
flask run
```
you should see a line in terminal telling you that localhost:5000/ is running

## Using the application
1. there are two student survey files in the uploads folder of the application.

2. copy and paste these on your desktop (or any other folder of your choice)

3. delete the student survey files from the application's uploads folder

4. when you run the application, select the student survey files that you copied and pasted elsewhere. You will see that the application takes in the files from your hard drive and saves it to the applications uploads folder -> this demonstrates that the system can take in an input file from the front-end HTML code and send it to the back-end.

5. go through the rest of the screens that validate, de-identify, clean, and re-validate the data.

6. click on data export to have the cleaned data set exported in the uploads folder as an excel file.

7. click on analysis to create two json files of analyses statistics and network objects in the uploads folder. The analysis results will also print on screen.
