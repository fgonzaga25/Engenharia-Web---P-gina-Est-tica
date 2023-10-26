import os

new_directory = "novo_diretorio"

try:
    os.mkdir(new_directory)
    print(f"Diretório '{new_directory}' criado com sucesso!")

except FileExistsError:
    print(f"O diretório '{new_directory}' já existe.")