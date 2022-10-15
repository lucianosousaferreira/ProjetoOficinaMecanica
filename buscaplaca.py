import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


headers = {
    
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
}

def PesquisaPlaca(url: str, placa: str) -> str:
    global arquivo
    response = requests.get(url=url + placa, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find('table',class_='fipeTablePriceDetail')
    str_tabela = str(tabela)
    df_table = pd.read_html(str_tabela)[0]

    try:
        mask_uf = df_table[0]=='UF:'
        uf = df_table[mask_uf][1]
        uf = uf.values[0]
    except Exception as ex:
        uf = '-'
    try:
        mask_municipio = df_table[0]=='Município:'
        municipio = df_table[mask_municipio][1]
        municipio = municipio.values[0]
    except Exception as ex:
        municipio = '-'
    
    try:
        mask_marca = df_table[0]=='Marca:'
        marca = df_table[mask_marca][1]
        marca = marca.values[0]
    except Exception as ex:
        marca = '-'
    
    try:
        mask_modelo = df_table[0]=='Modelo:'
        modelo = df_table[mask_modelo][1]
        modelo = modelo.values[0]
    except Exception as ex:
        modelo = '-'
    try:
        mask_comb = df_table[0]=='Combustível:'
        combustivel = df_table[mask_comb][1]
        combustivel = combustivel.values[0]
    except Exception as ex:
        combustivel = '-'
    try:
        mask_cor = df_table[0]=='Cor:'
        cor = df_table[mask_cor][1]
        cor = cor.values[0]
    except Exception as ex:
        cor = '-'
    try:
        mask_ano = df_table[0]=='Ano:'
        ano = df_table[mask_ano][1]
        ano = ano.values[0]
    except Exception as ex:
        ano = '-'
        
    dic_informacao = {
                        "Marca": marca,
                        "Modelo": modelo,
                        "Combustivel": combustivel,
                        "Cor": cor,
                        "Ano": ano,
                        "UF":uf,
                        "Municipio":municipio
                     }
    
    
    arquivo = json.dumps(dic_informacao,indent=4)
    
    return print(arquivo)

url = 'https://www.keplaca.com/placa/'
placa = 'HTY7443'
PesquisaPlaca(url=url,placa=placa)