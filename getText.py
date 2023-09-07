from newspaper import Article
import pandas as pd
import sys
import time

# Funzione per stampare la barra di avanzamento
def print_loading_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow}{spaces}] {int(progress * 100)}%')
    sys.stdout.flush()

# Nuovo dataframe
newDf = pd.DataFrame()

df = pd.read_csv('dataframeWithLinksClean.csv', encoding='utf8')

total_news = len(df['Url'])
processed_news = 0

for idx, news in enumerate(df['Url']):
    try:
        all_links = []
        topic = df.loc[df['Url'] == news, 'Topics'].iloc[0]
        score = df.loc[df['Url'] == news, 'Score'].iloc[0]
        parentDomain = df.loc[df['Url'] == news, 'Domain'].iloc[0]
        article = Article(news)
        article.download()
        article.parse()

        if article.text is None:
            continue
        
        # Controllo sulla lunghezza del testo
        if len(article.text.split()) < 100:
            continue
        data = {
            'Domain': [parentDomain] if parentDomain else [None],
            'Url': [news] if news else [None],
            'Score': [score] if score else [None],
            'Topics': [topic] if topic else [None],
            'Title': [article.title] if article and article.title else [None],
            'Authors': [article.authors] if article and article.authors else [None],
            'Publish date': [article.publish_date] if article and article.publish_date else [None],
            'Text': [article.text] if article and article.text else [None],
        }


        new_data_df = pd.DataFrame(data)
        print(data)
        # Concatena il dataframe esistente con il nuovo dataframe
        newDf = pd.concat([newDf, new_data_df], ignore_index=True)
        newDf.to_csv('nuoviArticoli.csv', index=False)
        
        processed_news += 1
        print_loading_bar(processed_news, total_news)
        
    except:
        continue

print('\nProcesso completato!')
