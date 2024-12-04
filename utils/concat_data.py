import pandas as pd

df1 = pd.read_csv('../data/graph_training_data.csv')
df2 = pd.read_csv('../data/nosql_training_data.csv')
df3 = pd.read_csv('../data/rdbms_training_data.csv')

df4 = df1._append(df2, ignore_index=True)
df5 = df4._append(df3, ignore_index=True)
df5.to_csv('data/final_training_data.csv')