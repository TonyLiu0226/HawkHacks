import pandas as pd
import random

with open("../backend/data/languages.txt","r") as file:
    langs = file.read().splitlines()

with open("../backend/data/frameworks.txt","r") as file:
    frameworks = file.read().splitlines()


cols =  langs + frameworks
user_df = pd.DataFrame()
user_df["Email"] = [f"{i}@lol.com" for i in range(100_000)]

for col in cols:
    user_df[col] = [random.randint(0,1) for i in range(100_000)]

user_df.to_csv("data.csv")