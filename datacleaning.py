import pandas as pd
import numpy as np

# df = pd.read_csv('automated.csv')
# df = pd.read_csv('nonautomatedAccountData.csv')
# df = pd.read_csv('realAccountData.csv')
df = pd.read_csv('fakeAccountData.csv')

df.isnull().sum()

# df.dropna(inplace=True)

# df.fillna(value, inplace=True)

# df.drop_duplicates(inplace=True)

# df['column_name'] = df['column_name'].astype('desired_data_type')

# df = pd.get_dummies(df, columns=['categorical_column'])

# df.to_csv('cleaned_data.csv', index=False)

