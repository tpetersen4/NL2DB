import pandas as pd

df1 = pd.read_csv('../data/nosql/query_explaination/output_all.csv')
df2 = pd.read_csv('../data/graph/query_explaination/output_all.csv')
df3 = pd.read_csv('../data/rdbms/query_explaination/output_all.csv')

df4 = df1._append(df2, ignore_index=True)
df5 = df4._append(df3, ignore_index=True)
df5.to_csv('../data/final_training_data_explanation.csv', index=False)

# k = [0, 1, 2, 3, 4, 5,6, 7,8, 10, 11, 12, 13, 16, 18, 19]
# k = range(14)
# k = [0, 1, 2, 4, 5, 6, 7, 8, 11, 12]
#
# df = pd.DataFrame(columns=['nl_query', 'explanation', 'db'])
# for i in k:
#     new_df = pd.read_csv(f'../data/nosql/query_explaination/output_{i}.csv')
#
#     df = df._append(new_df, ignore_index=True)
#
# df.to_csv('../data/nosql/query_explaination/output_all.csv', index=False)

