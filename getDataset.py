import pandas as pd

newsguard = pd.read_csv('newsguard.csv', encoding='utf8')
topics = ['Conspiracy theories or hoaxes', 'Sports and athletics', 'Health or medical information', 'Political news or commentary']
df = newsguard[newsguard['Topics'].isin(topics)]
df = df.loc[(df['Language'] == 'en') & (df['Paywall'] == 'No') & ((df['Domain'] == df['Parent Domain']) | df['Parent Domain'].isna())]
df = df[['Domain', 'Topics', 'Score']]
df = df.dropna(subset=['Score'])
file_path = 'dataframe.csv'
df.to_csv(file_path, index=False)