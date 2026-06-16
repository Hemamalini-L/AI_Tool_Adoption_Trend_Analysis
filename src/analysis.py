import pandas as pd

df = pd.read_csv(
    "../data/AI_Tool_Adoption_Dataset_5000.csv"
)

print(df.head())

print(df.describe())
