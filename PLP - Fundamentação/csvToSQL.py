import xml.etree.ElementTree as ET

# Carrega o arquivo XML
tree = ET.parse("pessoas.xml")
root = tree.getroot()

# Cria um arquivo SQL de Criação
with open("pessoas.sql", "w") as sqlfile:
    sqlfile.write("CREATE TABLE PESSOAS (\n")
    sqlfile.write("    COD INT PRIMARY KEY,\n")
    sqlfile.write("    GENERO CHAR(1),\n")
    sqlfile.write("    PESO FLOAT,\n")
    sqlfile.write("    ALTURA FLOAT\n")
    sqlfile.write(");\n")
    
    # Insere os dados das pessoas no SQL
    for pessoa in root.findall("PESSOA"):
        codigo = pessoa.find("COD").text
        genero = pessoa.find("GENERO").text
        peso = pessoa.find("PESO").text
        altura = pessoa.find("ALTURA").text
        
        sqlfile.write(f"INSERT INTO PESSOAS (COD, GENERO, PESO, ALTURA) VALUES ({codigo}, '{genero}', {peso}, {altura});\n")