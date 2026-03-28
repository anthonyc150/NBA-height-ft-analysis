import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df1 = pd.read_csv("data/Players.csv")
df2 = pd.read_csv("data/PlayerStatistics.csv")

print("File 1")
print(df1.shape)
print(df1.columns.tolist())
print(df1.head())

print("\nFile 2")
print(df2.shape)
print(df2.columns.tolist())
print(df2.head())
