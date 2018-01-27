import pandas as pd
import matplotlib.pyplot as plt
import csv

date_name = ['comment', 'date']
df = pd.read_csv('comments.csv', header=None, names=date_name, encoding='GB18030')
df['date'] = pd.to_datetime(df['date'])
print(df['date'].value_counts())

df.to_csv('test.txt', encoding='utf-8', index=False)
print(df.size)
