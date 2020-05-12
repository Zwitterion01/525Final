import pandas as pd
data = pd.read_json('data.json', lines=True)
print(data.head())
print(data.columns)
n_records = data.category.value_counts()
print(n_records)



