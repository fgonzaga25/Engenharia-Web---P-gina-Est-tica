import csv
import xml.etree.ElementTree as ET

# Carrega o arquivo XML
tree = ET.parse("pessoas.xml")
root = tree.getroot()

# Abre o arquivo CSV para escrita
with open("pessoas.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escreve o cabeçalho do CSV
    csvwriter.writerow(["COD", "GENERO", "PESO", "ALTURA"])
    
    # Escreve os dados das pessoas no CSV
    for pessoa in root.findall("PESSOA"):
        codigo = pessoa.find("COD").text
        genero = pessoa.find("GENERO").text
        peso = pessoa.find("PESO").text
        altura = pessoa.find("ALTURA").text
        
        csvwriter.writerow([codigo, genero, peso, altura])