import pandas as pd


df = pd.read_csv("data171.csv")
x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

# filter BETWEEN []
# Находим все координаты попавшие в квадрат x1,y1 - x2,y2
filter_df = df['x'].between(x1, x2) & df['y'].between(y2, y1)

print(df[filter_df])
