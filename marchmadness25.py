import pandas as pd
import numpy as np

df = pd.read_csv("summary25_pt.csv")

print(df.head())

df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df.dropna(subset=["seed"])
print(df.head())

df = df.sort_values(by="seed")
print(df.head())