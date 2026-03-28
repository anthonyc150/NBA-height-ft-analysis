import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))

df1 = pd.read_csv(os.path.join(base_dir, "data", "Players.csv"))
df2 = pd.read_csv(os.path.join(base_dir, "data", "PlayerStatistics.csv"), low_memory=False)

# Check how many rows drop when we remove missing heights
print(f"File 1 total rows: {len(df1)}")
print(f"File 1 rows with height: {df1['heightInches'].notna().sum()}")

# Check person_id overlap between both files
df2_ids = set(df2['personId'].dropna().astype(int))
df1_ids = set(df1['personId'])
print(f"\nPlayers in File 2 that exist in File 1: {len(df2_ids.intersection(df1_ids))}")
print(f"Players in File 2 missing from File 1: {len(df2_ids - df1_ids)}")

#looks at the missing players and cleans the data for the ones that have a NaN
#personID and prints the top 3
missing_ids = df2_ids - df1_ids
df2_clean = df2[df2['personId'].notna()].copy()
df2_clean['personId'] = df2_clean['personId'].astype(int)
missing_players = df2_clean[df2_clean['personId'].isin(missing_ids)][['firstName', 'lastName', 'personId']].drop_duplicates()
print(missing_players.head(3))

#merge the two dataframes on personId
df2_clean['personId'] = df2_clean['personId'].astype(int)
merged = df2_clean.merge(df1[['personId', 'heightInches']].dropna(), on='personId')

#check how many players have at least 50 free throw attempts total
ft_qualified = merged.groupby('personId')['freeThrowsAttempted'].sum()
print(f"Players with 50+ FT attempts: {(ft_qualified >= 50).sum()}")
print(f"Players with 25+ FT attempts: {(ft_qualified >= 25).sum()}")
print(f"Players with 10+ FT attempts: {(ft_qualified >= 10).sum()}")