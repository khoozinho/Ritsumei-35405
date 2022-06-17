import pandas as pd
titanic = pd.read_csv('titanic.csv')
print(titanic.head(8))
print(titanic.tail(10))

# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

ages = titanic["Age"]
print(ages.head())