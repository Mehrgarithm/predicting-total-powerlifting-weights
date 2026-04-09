# Purpose: fits the main multiple linear regression model uses a train-test split and evaluates the model with rmse and r^2 and compares training vs testing performance
import os
import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

INPUT_FILE_PATH=os.path.join("data", "processed", "powerlifting_model_ready.csv")
NOTES_FOLDER="notes"
SUMMARY_FILE_PATH=os.path.join(NOTES_FOLDER, "model_results_summary.txt")
os.makedirs(NOTES_FOLDER,exist_ok=True)
if not os.path.exists(INPUT_FILE_PATH):
    print("ERROR: Could not find model-ready dataset.")
    print("Expected location:", INPUT_FILE_PATH)
    raise FileNotFoundError(INPUT_FILE_PATH)
print("Loading model-ready dataset...")
df=pd.read_csv(INPUT_FILE_PATH)
print("Dataset loaded.")
print()
print("Dataset shape:")
print(df.shape)
print()
print("Columns:")
print(df.columns.tolist())
print()
#separates target and predictors
target_column="TotalKg"
if target_column not in df.columns:
    print("ERROR: Target column not found:", target_column)
    raise ValueError("Missing target column")
X=df.drop(columns=[target_column])
y=df[target_column]
print("Predictor matrix shape:")
print(X.shape)
print()
print("Target vector shape:")
print(y.shape)
print()
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("Training set size:" ,len(X_train))
print("Test set size:" ,len(X_test))
print()

#fit model
model=LinearRegression()
model.fit(X_train, y_train)
print("Model fitted.")
print()
# make predictions
y_train_pred=model.predict(X_train)
y_test_pred=model.predict(X_test)
# evaluation metrics
train_rmse=math.sqrt(mean_squared_error(y_train,y_train_pred))
test_rmse=math.sqrt(mean_squared_error(y_test,y_test_pred))
train_r2=r2_score(y_train,y_train_pred)
test_r2=r2_score(y_test,y_test_pred)
print("Training RMSE:",train_rmse)
print("Test RMSE:",test_rmse)
print()
print("Training R^2:",train_r2)
print("Test R^2:",test_r2)
print()
#collecting coefficients
coef_df = pd.DataFrame({"Variable":X.columns,"Coefficient":model.coef_})
coef_df=coef_df.sort_values(by="Coefficient",key=abs,ascending=False)
intercept_value=model.intercept_
print("Intercept:")
print(intercept_value)
print()
print("Top coefficients:")
print(coef_df)
print()


with open(SUMMARY_FILE_PATH, "w", encoding="utf-8") as f:
    f.write("MODEL RESULTS SUMMARY\n\n")
    f.write("Input dataset:\n")
    f.write(INPUT_FILE_PATH + "\n\n")
    f.write("Dataset shape:\n")
    f.write(str(df.shape) + "\n\n")
    f.write("Target variable:\n")
    f.write(target_column + "\n\n")
    f.write("Predictor variables:\n")
    for col in X.columns:f.write("- "+col+"\n")
    f.write("\n")
    f.write("Train-test split:\n")
    f.write("Training rows: "+str(len(X_train)) + "\n")
    f.write("Test rows: "+str(len(X_test)) + "\n")
    f.write("Test size proportion: 0.2\n")
    f.write("Random state: 42\n\n")
    f.write("Evaluation metrics:\n")
    f.write("Training RMSE: "+str(train_rmse) + "\n")
    f.write("Test RMSE: "+str(test_rmse) + "\n")
    f.write("Training R^2: "+str(train_r2) + "\n")
    f.write("Test R^2: "+str(test_r2) + "\n\n")
    f.write("Intercept:\n")
    f.write(str(intercept_value) + "\n\n")
    f.write("Coefficients:\n")
    f.write(coef_df.to_string(index=False))
    f.write("\n\n")
    f.write("Model equation form:\n")
    f.write("Predicted TotalKg = intercept + sum(coefficient_i * predictor_i)\n")
print("Model results summary saved to:")
print(SUMMARY_FILE_PATH)
print()
print("Model fitting and evaluation step finished.")