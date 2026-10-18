
# Algoritmo: Buscas
# Função: Exibir respostas para pesquisas
# Autor: Carolina
# Data: 18/10/2026

# Seção de Declarações
pesquisa = ""

# Início
# Seção de Comandos

print("O que deseja pesquisar? Opções: 1-Android 2-Windows 3-IOS")
pesquisa = input()

match pesquisa:
    case "1":
        print("Sistema utilizado pela maioria dos celulares no mundo.")

    case "2":
        print("Sistema Operacional da Microsoft usado na maioria dos computadores.")

    case "3":
        print("Sistema utilizado em celulares da marca Apple.")

    case _:
        print("Esse item não consta em nossa lista, tente novamente.")
