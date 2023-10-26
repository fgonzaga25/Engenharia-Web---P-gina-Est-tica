file_path = "exemplo.txt"

try:
    file = open(file_path, "r")
    content = file.read()
    file.close()
    print(content)

except FileNotFoundError:
    print("Arquivo não encontrado.")