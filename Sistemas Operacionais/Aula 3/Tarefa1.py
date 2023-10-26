import json
import os

# Cria uma lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa():
    # Solicita ao usuário para inserir uma descrição para a tarefa
    descrição = input("Insira uma descrição para a tarefa: ")

    # Cria uma nova tarefa com a descrição fornecida
    tarefa = {
        "id": len(tarefas) + 1,
        "descrição": descrição,
        "status": "pendente",
    }

    # Adiciona a nova tarefa à lista
    tarefas.append(tarefa)

# Função para listar todas as tarefas
def listar_tarefas():
    # Imprime o título do menu
    print("** Lista de Tarefas **")

    # Imprime todas as tarefas na lista
    for tarefa in tarefas:
        # Imprime o número de identificação da tarefa
        print("ID:", tarefa["id"])

        # Imprime a descrição da tarefa
        print("Descrição:", tarefa["descrição"])

        # Imprime o status da tarefa
        print("Status:", tarefa["status"])

# Função para marcar uma tarefa como concluída
def marcar_como_concluído():
    # Solicita ao usuário para inserir o número de identificação da tarefa
    id_tarefa = int(input("Insira o número de identificação da tarefa que deseja marcar como concluída: "))

    # Verifica se a tarefa existe
    if id_tarefa > len(tarefas) or id_tarefa < 1:
        print("Tarefa não encontrada.")
        return

    # Marca a tarefa como concluída
    tarefas[id_tarefa - 1]["status"] = "concluído"

# Função para excluir uma tarefa
def excluir_tarefa():
    # Solicita ao usuário para inserir o número de identificação da tarefa
    id_tarefa = int(input("Insira o número de identificação da tarefa que deseja excluir: "))

    # Verifica se a tarefa existe
    if id_tarefa > len(tarefas) or id_tarefa < 1:
        print("Tarefa não encontrada.")
        return

    # Exclui a tarefa da lista
    tarefas.pop(id_tarefa - 1)

# Função para salvar a lista de tarefas em um arquivo
def salvar_tarefas():
    # Abre o arquivo para escrita
    with open("tarefas.txt", "w") as arquivo:
        # Escreve a lista de tarefas no arquivo
        arquivo.write(json.dumps(tarefas))

# Função para carregar a lista de tarefas de um arquivo
def carregar_tarefas():
    # Abre o arquivo para leitura
    with open("tarefas.txt", "r") as arquivo:
        # Lê a lista de tarefas do arquivo
        tarefas = json.loads(arquivo.read())

# Menu principal
def menu():
    # Exibe o menu de opções
    print("** Menu de opções **")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluído")
    print("4. Excluir tarefa")
    print("5. Salvar tarefas")
    print("6. Carregar tarefas")
    print("0. Sair")

    # Solicita ao usuário para escolher uma opção
    opcao = int(input("Insira sua opção: "))

    # Executa a opção escolhida
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        marcar_como_concluído()
    elif opcao == 4:
        excluir_tarefa()
    elif opcao == 5:
        salvar_tarefas()
    elif opcao == 6:
        carregar_tarefas()
    elif opcao == 0:
        print("Saindo...")
        return