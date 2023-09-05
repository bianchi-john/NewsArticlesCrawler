import pandas as pd
df = pd.read_csv('dataframeWithLinksClean.csv', encoding='utf8')

count = df['Domain'].unique()

print (len(count))

print(len(df))