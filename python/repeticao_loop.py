
# Algoritmo: Repetição
# Função: Utilizar exemplo de Loop
# Autor: Carolina
# Data: 18/10/2026

# Seção de Declarações
produtoLoja = ""
loop = ""

# Início
# Seção de Comandos

print("Digite o nome do Produto:")
produtoLoja = input()

print("Deseja inserir mais um cadastro? SIM/NAO")
loop = input()

while loop == "sim":
    print("Digite o nome do Produto:")
    produtoLoja = input()

    print("Deseja inserir mais um cadastro? SIM/NAO")
    loop = input()

print("Cadastros realizados com sucesso!")
print("Obrigado por utilizar o programa")
