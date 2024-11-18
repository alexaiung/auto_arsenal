import pandas as pd
from bs4 import BeautifulSoup

print('Executing...')

file_path = r"C:/Users/med-pediatria/Desktop/relatorios_arsenal/2024-01-04.html"
with open(file_path, 'r') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')

total_paginas = soup.find('span', id='f3a0a452')
total_paginas = int(total_paginas.get_text().strip())
print('Total de páginas:', total_paginas)
categorias_pedidos = ['Avulsos', 'Produtos']

cod_paginas = ['f1a0a452', 'f1a792a452', 'f1a1584a452']
for cod_pag in cod_paginas:
    pag = soup.find('span', id=cod_pag)
    if pag != None:
        pag = int(pag.get_text().strip())
        print('=' * 50)
        print('Página', pag)
        print('=' * 50)

        pedidos = soup.find_all('span', id='f3')
        pedidos = [pedido.get_text() for pedido in pedidos if pedido.get_text() in categorias_pedidos]
        
        for i, pedido in enumerate(pedidos):
            print('Pedido nº' + str(i+1) + ": " + pedido)
        print('-' * 50)

            
pedidos = []
produtos = soup.find_all('span', id='f2')
produtos = [produto.get_text() for produto in produtos]
# posicoes_pedidos = [produto.index() for produto in produtos if produto == "Quantidade"]
print(posicoes_pedidos)