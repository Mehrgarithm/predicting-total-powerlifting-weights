#Purpose:is to load the raw open powerlifting dataset to keep only the columns that matter for this project by applying simple filtering rules and remove duplicate rows and measure missing values to save a clean working dataset for later use
import os
import pandas as pd

# made the following few lines to make sure the right file is selected if the TA obtains a different name for the files by using file path and also 
# double checks the name
RAW_FILE_NAME="openpowerlifting.csv"
RAW_FILE_PATH=os.path.join("data","raw",RAW_FILE_NAME)
PROCESSED_FOLDER=os.path.join("data","processed")
PROCESSED_FILE_PATH=os.path.join(PROCESSED_FOLDER,"powerlifting_working.csv")
NOTES_FILE_PATH=os.path.join("notes","cleaning_summary.txt")
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs("notes", exist_ok=True)
if not os.path.exists(RAW_FILE_PATH):
    print("ERROR: raw dataset file not found.")
    print("Expected location:",RAW_FILE_PATH)
    raise FileNotFoundError(RAW_FILE_PATH)
#loading the raw dataset
print("Loading raw dataset...")
df=pd.read_csv(RAW_FILE_PATH,low_memory=False)
print("Raw dataset loaded.")
#save original size for the summary
original_rows, original_cols = df.shape

#check which useful columns exist
wanted_columns = ["Sex", "Event" ,"Equipment","Age","BodyweightKg", "TotalKg", "Dots", "Tested", "Division", "WeightClassKg"]
existing_columns = []
missing_columns = []
for col in wanted_columns:
    if col in df.columns:
        existing_columns.append(col)
    else:
        missing_columns.append(col)
print("Columns found for possible use:")
for col in existing_columns:
    print("  ", col)
print()
print("Columns not found:")
for col in missing_columns:
    print("  ", col)
print()
#keep only the useful columns that actually exist
df=df[existing_columns].copy()
print("Shape after keeping useful columns only:")
print(df.shape)
print()


#removing duplicate rows
duplicate_count = df.duplicated().sum()
df=df.drop_duplicates()
print("Duplicate rows removed:",duplicate_count)
print("Shape after removing duplicates:")
print(df.shape)
print()
required_basic_columns = ["Sex","Equipment","BodyweightKg","TotalKg","Dots"]

for col in required_basic_columns:
    if col in df.columns:
        df=df[df[col].notna()]
print("Shape after dropping rows missing required basic columns:")
print(df.shape)
print()

# filter positive numeric values
if "BodyweightKg" in df.columns:df=df[df["BodyweightKg" ]>0]
if "TotalKg" in df.columns:df=df[ df["TotalKg"]>0]
print("Shape after filtering positive BodyweightKg and TotalKg:")
print(df.shape)
print()

#filter full powerlifting event rows if the event column exists
#sbd is the common code for full powerlifting total
if "Event" in df.columns:
    before_event_filter=df.shape[0 ]
    df=df[ df["Event"]=="SBD"]
    after_event_filter=df.shape[0]

    print("Rows before Event filter:",before_event_filter)
    print("Rows after keeping only Event =='SBD':",after_event_filter)
    print()
else:
    print("Event column not found, so no Event filter was applied.")
    print()

# check missing values after filtering
missing_counts=df.isna().sum()
print("Missing values after filtering:")
print(missing_counts)
print()
df.to_csv(PROCESSED_FILE_PATH, index=False)
print("Cleaned working dataset saved to:")
print(PROCESSED_FILE_PATH)
print()

#summary of the cleaning
with open(NOTES_FILE_PATH, "w", encoding="utf-8") as f:
    f.write("CLEANING SUMMARY\n\n")
    f.write("Original dataset shape:\n")
    f.write(f"{original_rows} rows, {original_cols} columns\n\n")
    f.write("Columns kept for project work:\n")
    for col in existing_columns:f.write(f"{col}\n")
    f.write("\n")
    f.write("Columns requested but not found:\n")
    for col in missing_columns:f.write(f"{col}\n")
    f.write("\n")
    f.write(f"Duplicate rows removed: {duplicate_count}\n\n")
    f.write("Final cleaned dataset shape:\n")
    f.write(f"{df.shape[0]} rows, {df.shape[1]} columns\n\n")
    f.write("Missing value counts after filtering:\n")
    f.write(missing_counts.to_string())
    f.write("\n")
print("Cleaning summary saved to:")
print(NOTES_FILE_PATH)
print()
print("Cleaning finished successfully.")