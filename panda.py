import pandas as pd


df = pd.DataFrame({
        "Name": ["Braund, Mr. Owen Harris",
                                   "Allen, Mr. William Henry",
              "Bonnell, Miss. Elizabeth"],
     "Age": [22, 35, 58],
                    "Sex": ["male", "male", "female"]}
 )

#print(df)

#print(df["Age"])
ages = pd.Series([22, 35, 58], name="Age")
print(ages)

#print(df["Age"].max())
print(ages.max())

print(df.describe())
titanic = pd.read_csv("titanic.csv")
print(titanic.head(8))
#print(titanic.dtypes)

#print(titanic.info())

ages = titanic["Age"]
print(ages.head())

above_35 = titanic[titanic["Age"] > 35]

print(above_35.head())

print(titanic["Age"] > 35)

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]

print(class_23.head())

age_no_na = titanic[titanic["Age"].notna()]

print(age_no_na.head())