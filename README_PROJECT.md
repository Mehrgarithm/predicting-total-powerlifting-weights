CMPUT 195 Mini Project

Group Members:
Person 1: Abdul Rafai Ahmad
Person 2: Edwin Shaiju David

Project:
Predicting Powerlifting Total from Bodyweight, Age, Sex, and Equipment, with Secondary Analysis of DOTS

goal of the project: this project is meant to use the publicly available data so we may be able to predict how much an athletes will lift (total) in the competition using knowledge of their weight, age, sex, and equipment category and double checks this using the DOTS as a secondary analysis variable to compare relative and absolute strength

Research question(s):
1.how accurately can an athletes competition total be predicted using bodyweight, age, sex, and equipment category?
2. how do these same variables relate to relative strength as measured by DOTS?

Github for project: https://github.com/Mehrgarithm/predicting-total-powerlifting-weights
                    this version has things such as available graphs and descriptions and notes and summaries and figures
Folder Structure:
data/raw= raw downloaded dataset (contains .zip and .csv)
data/processed= for the cleaned and processed datasets created during the project
code= programming files to work with the data
figures= saved graphs and visual outputs
notes= plannings and notes and summary files
report= report outline and later report file

Data source: Official OpenPowerlifting bulk csv dataset
Working dataset: the raw dataset is stored in data/raw/ and is hidden by gitignore but a cleaned working dataset is created from it and saved in data/processed/ for later analysis, visualization, and modeling this is not hidden by the gitignore file

Whats been done so far:
- repo created
- collaborator added
- folder/directory structure created
- Research questions and information written with basic report outline created
- Added data source and gitignore file.
- Official Open Powerlifting bulk data set selected
- Raw dataset downloaded and placed in data/raw/
- Raw dataset extracted locally
- Data source note created
- .gitignore created and updated for raw data handling
- Initial Python dataset loading and inspection completed
- Dataset shape checked
- Column names checked
- Data types checked
- Missing values checked
- Required project columns checked
- Dataset summary file created
- Cleaning and filtering script created
- Relevant project columns selected for working use
- Duplicate rows checked and removed if present
- Required missing values filtered
- Invalid BodyweightKg and TotalKg rows filtered
- Event filtering applied for full powerlifting rows if available
- Cleaned working dataset created in data/processed/
- Cleaning summary file created
- model-preparation script was written and ran
- final model-ready dataset was created
- model-preparation summary note was created
- Mathematical model summary note was created.
- Evaluation interpretation note was created.

required python libraries so far:
 - pandas
 - numpy
 - math 
 - matplotlib
 - sklearn

How to Run the Current Code:
1. Make sure you have all the python libraries mentioned above installed 
2. Ensure that the raw OpenPowerlifting CSV file is inside data/raw/ and named the exact way as as it is in what is on line 7 of file 01_load_and_inspect.py
3. Make sure the file name in code/01_load_and_inspect.py (line 7) matches the real CSV file name
4. Open the project folder in terminal
5. Run:
   python3 code/01_load_and_inspect.py
6. Run:
   python3 code/02_clean_and_filter.py
7. Run:
   python3 code/03_eda.py
8. Run:
   python3 code/04_prepare_model_data.py
9. Run:
   python3 code/05_fit_and_evaluate_model.py


Important Notes:
- All file paths in the code use paths relative to the project folder
- The raw dataset file must be placed inside data/raw/
- The exact raw CSV file name in the Python code must match the real file name in data/raw/
- Summary text files may be overwritten when scripts are run again this is expected and should not cause an error by itself
- Cleaned and made the summarized the files may be replaced with updated versions when the python files are run again
