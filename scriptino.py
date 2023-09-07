import pandas as pd
df = pd.read_csv('dataframeWithLinksAndTextClean.csv', encoding='utf8')

# Ottenere i valori distinti dalla colonna "Domain" e il loro "Topics" associato
distinct_domains = df['Domain'].unique()
Political = 0
Conspiracy = 0
Sports = 0
Health = 0
for domain in distinct_domains:
    topics_for_domain = df[df['Domain'] == domain]['Topics'].unique()
    print(f'Domain: {domain}')
    print(f'Topics: {", ".join(topics_for_domain)}')
    print()
    if (topics_for_domain =="Political news or commentary" ):
        Political = Political + 1
    if (topics_for_domain == "Conspiracy theories or hoaxes"):
        Conspiracy = Conspiracy + 1
    if (topics_for_domain == "Sports and athletics"):
        Sports = Sports + 1
    if (topics_for_domain == "Health or medical information"):
        Health = Health + 1

print ("Political " + str(Political))
print ("Conspiracy " + str(Conspiracy))
print ("Healt " + str(Health))
print ("Sport " + str(Sports))
