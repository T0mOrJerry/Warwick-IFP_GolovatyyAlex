import pandas as pd
df = pd.read_csv('customers.csv')

print(df.describe())
print(df.size)
print(df.shape)
# No missing values
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.describe())
print(df)
print(df.corr(numeric_only=True))
