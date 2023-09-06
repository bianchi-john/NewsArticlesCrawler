import pandas as pd

import pandas as pd
df = pd.read_csv('dataframeWithLinksAndText.csv', encoding='utf8')

# Supponiamo che il tuo DataFrame si chiami df
# Sostituisci '\n' con uno spazio vuoto nella colonna "Text"
df['Text'] = df['Text'].str.replace('\n', ' ')
df.drop_duplicates(subset='Url', keep='first', inplace=True)

df.to_csv('dataframeWithLinksAndTextClean.csv', index=False)
