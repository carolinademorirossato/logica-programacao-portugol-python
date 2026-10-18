
# Algoritmo: Análise de notas
# Função: Verificar se a pessoa está aprovada ou não
# Autor: Carolina
# Data: 18/10/2026

# Seção de Declarações
estudante = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0
presencas = 0

# Início
# Seção de Comandos

print("Digite o nome do(a) estudante")
estudante = input()

print("Insira a primeira nota:")
nota1 = float(input())

print("Insira a segunda nota:")
nota2 = float(input())

print("Qual a frequência do(a) aluno(a):")
presencas = int(input())

media = (nota1 + nota2) / 2

print("Resultado:", media)

if media >= 7 and presencas >= 80:
    print("Parabéns, você foi aprovado(a)!")
else:
    print("Infelizmente você foi reprovado(a)!")
