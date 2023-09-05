import pandas as pd
import tldextract

df = pd.read_csv('dataframeWithLinks.csv', encoding='utf8')

# Funzione per estrarre il dominio da un URL
def extract_domain(url):
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

# Estrarre il dominio dalla colonna "Url" e confrontarlo con la colonna "Domain"
df["Extracted_Domain"] = df["Url"].apply(extract_domain)
df = df[df["Extracted_Domain"] == df["Domain"]]

# Eliminare la colonna "Extracted_Domain" se non è più necessaria
df.drop(columns=["Extracted_Domain"], inplace=True)

# Ora df contiene solo le righe con URL che fanno riferimento alla testata giornalistica corretta
print(df)
# Filtrare il dataframe per escludere le righe con "author" o "category" nella colonna "Url"
df = df[~df["Url"].str.contains("author|category|@|.jpg|.png|.jpeg|.pdf|.zip|.gif|.mp4")]


df.to_csv('dataframeWithLinksClean.csv', index=False)

print('Done')