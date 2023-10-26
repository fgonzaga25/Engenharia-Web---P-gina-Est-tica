import random
import xml.etree.ElementTree as ET
import numpy as np

# Cria uma função para gerar os dados de acordo com as distribuições especificadas
def gera_dados_pessoa():
    genero = random.choice(['M', 'F'])
    codigo = random.randint(1, 10000)
    
    if genero == 'M':
        peso = np.random.normal(76, 10)
        altura = np.random.normal(1.78, 0.10)
    else:
        peso = np.random.normal(65, 8)
        altura = np.random.normal(1.68, 0.11)
    
    return genero, codigo, peso, altura

# Cria o elemento raiz do XML
root = ET.Element("DADOS")

# Preenche o XML com os dados de 10.000 pessoas
for _ in range(10000):
    genero, codigo, peso, altura = gera_dados_pessoa()
    
    pessoa = ET.SubElement(root, "PESSOA")
    ET.SubElement(pessoa, "COD").text = str(codigo)
    ET.SubElement(pessoa, "GENERO").text = genero
    ET.SubElement(pessoa, "PESO").text = str(round(peso, 2))
    ET.SubElement(pessoa, "ALTURA").text = str(round(altura, 2))

# Cria o arquivo XML
tree = ET.ElementTree(root)
tree.write("pessoas.xml")