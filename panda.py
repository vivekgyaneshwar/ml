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
print(titanic.dtypes)
titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)
titanic = pd.read_excel('titanic.xlsx', sheet_name='passengers')
print(titanic.info())