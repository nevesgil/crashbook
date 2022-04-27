# example

import pandas as pd

aliens_feat = {
    "alien1": {"name": "bob", "age": 1},
    "alien2": {"name": "jaci", "age": 2},
    "alien3": {"name": "mika", "age": 3},
    "alien4": {"name": "dave", "age": 4},
    "alien5": {"name": "mussum", "age": 5},
}

data = []
for key, value in aliens_feat.items():
    data.append(value)

df = pd.DataFrame.from_dict(data)

# print(df)

ss = aliens_feat.get("dd", "blablablablablabla")

print(ss)
