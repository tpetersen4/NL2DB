import pandas as pd

dry_run = True

filename = "../data/nosql/query_explaination/output_12.txt"

with open(filename, "r") as f:
    lines = []
    count = 0
    nl_query, explanation = [], []
    for line in f:
        if line != '\n':
            lines.append(line)
    for line in lines:
        if count % 2 == 0:
            l = line.split("**")
            l = l[1].replace('"', '').replace('\n', '')
            nl_query.append(str(l))
        else:
            l = line.replace('\n', '').replace('"', '')
            explanation.append(str(l))
        count += 1

df = pd.DataFrame({'nl_query': nl_query, 'explanation': explanation, 'db': 'nosql'})
df.to_csv("../data/nosql/query_explaination/output_12.csv", index=False)

# df_old = pd.read_csv("../data/rdbms/query_explaination/output.csv")

# df_old = df_old._append(df, ignore_index=True)
# print(df_old.head())
# if not dry_run:
#     df_old.to_csv("../data/rdbms/query_explaination/output.csv", index=False)
