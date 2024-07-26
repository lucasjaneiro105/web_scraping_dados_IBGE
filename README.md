# Scraping de Indicadores do IBGE

Este projeto realiza o scraping dos indicadores econômicos do site do IBGE e salva os dados em um arquivo CSV.

## Descrição

O script acessa a página de indicadores do IBGE, extrai informações sobre diversos indicadores econômicos e organiza esses dados em um DataFrame do Pandas. Os dados são então limpos e salvos em um arquivo CSV.

## Requisitos

- Python 3.x
- Bibliotecas: BeautifulSoup, pandas, requests

Você pode instalar as bibliotecas necessárias usando o comando:

```bash
pip install beautifulsoup4 pandas requests
