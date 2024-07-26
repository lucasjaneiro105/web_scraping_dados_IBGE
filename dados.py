# Bibliotecas 
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Scraping dos indicadores do IBGE
def scraping_ibge():
    # URL da página de indicadores do IBGE
    url = "https://www.ibge.gov.br/indicadores.html"
    # Cabeçalho para simular um navegador
    browsers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    # Realiza a requisição à página
    page = requests.get(url, headers=browsers)
    # Parse do conteúdo HTML da página
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Filtrando e Organizando os dados 
    titulos = soup.find_all('span', {'class': 'nonsprite'})
    meses = soup.find_all('td', {'class': 'desktop-tablet-only dozemeses'})
    ano = soup.find_all('td', {'class': 'desktop-tablet-only ano'})
    
    indicadores = [(titulo.text.strip(), mes.text.strip(), ano.text.strip()) for titulo, mes, ano in zip(titulos, meses, ano)]
    
    return indicadores

# Realizando o scraping
indicadores = scraping_ibge()

# Criando um DataFrame e fazendo o tratamento dos dados
df = pd.DataFrame(indicadores, columns=['Indicadores', 'Meses', 'Ano'])

df['Meses'] = df['Meses'].str.replace('12 meses\r\n', '')
df['Ano'] = df['Ano'].str.replace('No ano\r\n', '')
df['Meses'] = df['Meses'].str.strip()
df['Ano'] = df['Ano'].str.strip()

df = df[(df['Meses'] != '-') & (df['Ano'] != '-')]

# Salvando o df em um arquivo CSV
df.to_csv('indicadores_ibge.csv', index=False)
