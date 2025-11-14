import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")

#print(df.head())

print("Inspection Report:")
for column in df.columns:
    dtype = df[column].dtype             
    missing = df[column].isnull().sum()  
    missingPerc = (missing / len(df)) * 100

    print(f"{column}: {dtype}, Missing: {missingPerc:.2f}%")

df['Age'] = df["Age"].fillna(df.groupby(["Pclass","Sex"])["Age"].transform("median"))

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode())

df.drop("Cabin", axis = 1)
df["Family Size"] = df["SibSp"] + df["Parch"]
df["IsAlone"] = df["Family Size"].apply(lambda x: 1 if x==0 else 0)
df
df['Age'] = df['Age'].astype(int)
df.dtypes
filename = "titanic_cleaned.csv" 
df.to_csv(filename, index=False)
print("File Saved")