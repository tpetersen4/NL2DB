import pandas as pd

df = pd.DataFrame(columns=['nl_query'])
for i in range(15):
    with open(f'data/graph/output_{i}.txt', 'r') as f:
        read = False
        kaim = []
        for line in f:
            if read and line != '\n':
                kaim.append(" ".join(line.split(' ')[1:]))
            if line == '\n':
                if read:
                    read = False
                else:
                    read = True

    df = df._append(pd.DataFrame({'nl_query': kaim}))

df['db'] = 'graph'
# print(df.head())
df.to_csv('data/graph_training_data.csv', index=False)