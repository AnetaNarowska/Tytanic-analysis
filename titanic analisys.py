import pandas as pd

df=pd.read_csv('tytanic.csv')

print(df.head())
print(df['Age'].mean())
print(df['Age'].max())
print(df['Age'].min())

print(df['Sex'].value_counts())

for index,row in df.iterrows():
  print(row['PassengerId'],row['Fare'])