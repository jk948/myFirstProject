import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data/world-bank-1_data.csv")

print(df.iloc[ : , 0:3])

print(df.iloc[0:3])

print(df.iloc[0])

le_min = df["life_expectancy_t"].min()
le_max = df["life_expectancy_t"].max()
print(df.loc[df["life_expectancy_t"] == le_min, "country"])

print(df.loc[df["life_expectancy_t"] == le_max, "country"])

countries = df.loc[df["country"] == "United Kingdom", ]
print(countries.shape)

uk_2020 = df.loc[(df["country"] == "United Kingdom") & (df["year"] == 2020), ]
print(uk_2020.shape)

df.plot(x="life_expectancy_f", y="life_expectancy_m")
plt.show()

df.plot.box(column="life_expectancy_m", )
plt.show()