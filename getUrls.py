from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import csv
import pandas as pd

#Nuovo dataframe
newDf = pd.DataFrame()

# Rimuovo i duplicati
def removeDuplicates(urls):
    urlsNoDuplicates = []
    for link in urls:
        try:
            urlsNoDuplicates.append(link.get_attribute('href'))
        except:
            continue
    return list(set(urlsNoDuplicates))


import time

# Funzione per estrarre e seguire i link (massimo 20 link)
def extract_and_follow_links(driver, url, max_links):
    driver.set_page_load_timeout(10)
    links_to_save = []  # Per tenere traccia dei link da salvare
    try:
        print(f"Caricamento della pagina: {url}")
        start_time = time.time()  # Registra il tempo di inizio
        driver.get(url)
        while True:
            elapsed_time = time.time() - start_time  # Calcola il tempo trascorso
            if elapsed_time >= 5:
                print("Il limite di 5 secondi è stato superato. Passo alla successiva.")
                break
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//a[@href]")))
                # Se si è verificato il caricamento entro 1 secondo, esci dal ciclo
                break
            except:
                # Se il caricamento non è ancora avvenuto, continua ad aspettare
                continue
        
        if elapsed_time < 5:
            print("La pagina è stata caricata con successo.")
            # Estrai e stampa tutti gli elementi <a> con il dominio del sito in questione
            links = driver.find_elements(By.XPATH, "//a[@href]")
            # Rimuovo i duplicati
            links = removeDuplicates(links)
            # Limite massimo di link da estrarre
            for link in links:
                if (domain in link):
                    links_to_save.append(link)  # Aggiungi il link da salvare alla lista
                    
                if len(links_to_save) >= max_links:
                    break  # Esci dal ciclo una volta raggiunto il limite massimo
            print(f"Numero di link estratti: {len(links_to_save)}")
        else:
            print("Tempo limite di 5 secondi superato. Passo alla successiva.")
        
        return links_to_save
    except Exception as e:
        print(f"Si è verificato un errore durante l'estrazione dei link: {str(e)}")
        return links_to_save



# Configura il driver di Chrome con il percorso specificato
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=en')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')


#chrome_options.add_argument('--headless')  # Esegui Chrome in modalità headless per velocizzare il processo
chrome_service = ChromeService(executable_path='/home/john/Vari/webdrivers/chromedriver')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
df = pd.read_csv('dataframe.csv', encoding='utf8')

for domain in df['Domain']:
    all_links = []
    topic = df.loc[df['Domain'] == domain, 'Topics'].iloc[0]
    score = df.loc[df['Domain'] == domain, 'Score'].iloc[0]
    fullDomain = 'https://www.' + domain
    links = extract_and_follow_links(driver, fullDomain, 20)
    all_links.extend(links)
    newsLinks = []
    for all_link in all_links:
        links = extract_and_follow_links(driver, all_link, 999)
        newsLinks.extend(links)
    newsLinks = list(set(newsLinks))
    data_list = []
    for news in newsLinks:
        data = {
            'Domain': domain,
            'Score': score,
            'Topics': topic,
            'Url': news,
        }
        data_list.append(data)
    # Crea un dataframe dai dati dei dizionari
    new_data_df = pd.DataFrame(data_list)
    # Concatena il dataframe esistente con il nuovo dataframe
    newDf = pd.concat([newDf, new_data_df], ignore_index=True)
    newDf.to_csv('dataframeWithLinks.csv', index=False)


newDf.to_csv('dataframeWithLinks.csv', index=False)

# Chiudi il driver di Chrome una volta completata l'operazione
driver.quit()
