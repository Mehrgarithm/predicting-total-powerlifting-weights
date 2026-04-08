#purpose of this file is to prepare the final model-ready dataset for the main regression model as it keeps the final chosen columns and drops rows with missing age and encodes categorical predictors
import os
import pandas as pd
INPUT_FILE_PATH=os.path.join("data","processed","powerlifting_working.csv")
OUTPUT_FOLDER=os.path.join("data","processed")
OUTPUT_FILE_PATH=os.path.join(OUTPUT_FOLDER,"powerlifting_model_ready.csv")
NOTES_FOLDER="notes"
SUMMARY_FILE_PATH=os.path.join(NOTES_FOLDER,"model_prep_summary.txt")
os.makedirs(OUTPUT_FOLDER,exist_ok=True)
os.makedirs(NOTES_FOLDER,exist_ok=True)

if not os.path.exists(INPUT_FILE_PATH):
    print("ERROR: Could not find cleaned working dataset.")
    print("Expected location:",INPUT_FILE_PATH)
    raise FileNotFoundError(INPUT_FILE_PATH)
print("Loading cleaned working dataset...")
df=pd.read_csv(INPUT_FILE_PATH,low_memory=False)
print("Dataset loaded.")
print()

#final chosen columns
required_columns=["TotalKg","BodyweightKg","Age","Sex","Equipment"]
for col in required_columns:
    if col not in df.columns:
        print("ERROR: Missing required column:", col)
        raise ValueError(f"Missing column: {col}")
model_df=df[required_columns].copy()
print("Columns selected for main model:")
print(model_df.columns.tolist())
print()

#missing value check before dropping
missing_before=model_df.isna().sum()
print("Missing values before dropping rows:")
print(missing_before)
print()
original_row_count=len(model_df)
# drop rows with missing values in main model columns
model_df=model_df.dropna(subset=required_columns).copy()
after_drop_row_count=len(model_df)
rows_removed=original_row_count-after_drop_row_count
print("Rows before dropping missing values:",original_row_count)
print("Rows after dropping missing values:",after_drop_row_count)
print("Rows removed:",rows_removed)
print()
#one-hot encode categorical variables
categorical_cols=["Sex", "Equipment"]
model_df=pd.get_dummies(model_df,columns=categorical_cols,drop_first=True)
print("Columns after one-hot encoding:")
print(model_df.columns.tolist())
print()
#standardizing numerical predictor where z=(x-mean)/std
numeric_predictor_cols=["BodyweightKg","Age"]
scaling_info={}
for col in numeric_predictor_cols:
    col_mean=model_df[col].mean()
    col_std=model_df[col].std()
    scaling_info[col]={"mean": col_mean ,"std": col_std}
    if col_std == 0:
        print("WARNING:",col,"has standard deviation 0. It will not be scaled.")
    else:
        model_df[col]=(model_df[col]-col_mean)/col_std
print("Numerical predictor columns manually standardized:")
print(numeric_predictor_cols)
print()

#save model-ready dataset
model_df.to_csv(OUTPUT_FILE_PATH, index=False)
print("Model-ready dataset saved to:")
print(OUTPUT_FILE_PATH)
print()
# write summary file
with open(SUMMARY_FILE_PATH,"w",encoding="utf-8") as f:
    f.write("MODEL PREPARATION SUMMARY\n\n")
    f.write("Input dataset:\n")
    f.write(INPUT_FILE_PATH+"\n\n")
    f.write("Final chosen main model columns before encoding:\n")
    for col in required_columns:f.write("- "+col+"\n")
    f.write("\n")
    f.write("Missing values before dropping rows:\n")
    f.write(missing_before.to_string())
    f.write("\n\n")
    f.write("Rows before dropping missing values:\n")
    f.write(str(original_row_count)+"\n\n")
    f.write("Rows after dropping missing values:\n")
    f.write(str(after_drop_row_count)+"\n\n")
    f.write("Rows removed:\n")
    f.write(str(rows_removed)+"\n\n")
    f.write("Categorical columns encoded:\n")
    for col in categorical_cols:f.write("- "+col+"\n")
    f.write("\n")
    f.write("Numerical predictor columns manually standardized using z-score:\n")
    for col in numeric_predictor_cols:f.write("- "+col+"\n")
    f.write("\n")
    f.write("Scaling values used:\n")
    for col in numeric_predictor_cols:
        f.write(col+" mean: "+str(scaling_info[col]["mean"])+"\n")
        f.write(col+" std: "+str(scaling_info[col]["std"])+"\n")
    f.write("\n")
    f.write("Final model-ready columns:\n")
    for col in model_df.columns:f.write("- "+str(col)+"\n")
    f.write("\n")
    f.write("Final model-ready dataset shape:\n")
    f.write(str(model_df.shape)+"\n")
print("Model preparation summary saved to:")
print(SUMMARY_FILE_PATH)
print()
print("Model preparation step finished.")