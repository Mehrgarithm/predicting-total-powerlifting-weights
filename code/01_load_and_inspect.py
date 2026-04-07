# Purpose:this file loads the raw OpenPowerlifting CSV file and preprocesses EDA and modeling

import os
import pandas as pd
# made the following few lines to make sure the right file is selected if the TA obtains a different name for the raw csv file by using file path and also 
# double checks the name
DATA_FILE_NAME ="openpowerlifting.csv"
DATA_FILE_PATH=os.path.join("data","raw",DATA_FILE_NAME)

if not os.path.exists(DATA_FILE_PATH):
    print("ERROR: The dataset file was not found.")
    print("Expected location:", DATA_FILE_PATH)
    print("Check the file name and make sure the CSV is inside data/raw/")
    raise FileNotFoundError(DATA_FILE_PATH)

# loads the csv into a pandas dataFrame
print("Loading dataset...")
df=pd.read_csv(DATA_FILE_PATH, low_memory=False)
print("Dataset loaded successfully.")
print()
# print the first few rows so we can see what one row looks like and the shape so we know what the data looks like so we can preprocess
print("FIRST 5 ROWS")
print(df.head())
print("-"*80)
print()
print("DATASET SHAPE")
print(df.shape)
print("-"*80)
print()


#prints the list of columns so that we can see what we need to confirm that the columns needed for the project exist
print("COLUMN NAMES")
for col in df.columns:
    print(col)
print("-"*80)
print()

#print data types and non null counts so we can see whether columns are numeric or text and whether there are missing values
print("DATAFRAME INFO")
print(df.info())
print("-"*80)
print()



# prints the summary statistics for numeric columns (mean, min, max, etc, etc)
print("NUMERICAL SUMMARY")
print(df.describe())
print("-" *80)
print()


# print missing-value counts
# Missing values matter for the preprocessing section of the project and checks to see whether the key project columns exist
print("MISSING VALUES BY COLUMN")
print(df.isna().sum())
print("-"*80)
print()
required_columns = [ "Sex","Event", "Equipment", "Age","BodyweightKg", "TotalKg", "Dots"]
print("REQUIRED COLUMN CHECK")
for col in required_columns:
    if col in df.columns:
        print(col, "->FOUND")
    else:
        print(col,"->MISSING")
print("-"*80)
print()
#saves a text summary to the notes folder so that itll be easier to use the results in the report later
notes_folder="notes"
os.makedirs(notes_folder ,exist_ok=True)
summary_file_path=os.path.join(notes_folder,"dataset_summary.txt")
with open(summary_file_path,"w",encoding="utf-8") as f:
    f.write("DATASET SUMMARY\n")
    f.write("\n")
    f.write("Dataset file path:\n")
    f.write(DATA_FILE_PATH+"\n\n")
    f.write("Dataset shape:\n")
    f.write(str(df.shape)+"\n\n")
    f.write("Required column check:\n")
    for col in required_columns:
        if col in df.columns:
            f.write(f"{col}: FOUND\n")
        else:
            f.write(f"{col}: MISSING\n")
    f.write("\n")
    f.write("Missing value counts:\n")
    f.write(df.isna().sum().to_string())
    f.write("\n")
print("A summary file has been saved to:")
print(summary_file_path)