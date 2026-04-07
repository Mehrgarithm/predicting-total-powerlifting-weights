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

Folder Structure:
data/raw= raw downloaded dataset (contains .zip and .csv)
data/processed= for the cleaned and processed datasets created during the project
code= programming files to work with the data
figures= saved graphs and visual outputs
notes= plannings and notes and summary files
report= report outline and later report file

Data source: Official OpenPowerlifting bulk csv dataset

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

required python libraries so far:
 - pandas

How to Run the Current Code:
1. Place the raw OpenPowerlifting CSV file inside data/raw/
2. Make sure the file name in code/01_load_and_inspect.py matches the real CSV file name
3. Open the project folder in terminal
4. Run:
   python3 code/01_load_and_inspect.py

Important Notes:
- All file paths in the code use paths relative to the project folder
- The raw dataset file must be placed inside data/raw/
- The exact raw CSV file name in the Python code must match the real file name in data/raw/
- Summary text files may be overwritten when scripts are run again this is expected and should not cause an error by itself
