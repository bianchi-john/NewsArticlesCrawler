import pandas as pd
df = pd.read_csv('dataframeWithLinks.csv', encoding='utf8')

count = df['Domain'].unique()

print (len(count))