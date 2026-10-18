algoritmo "Análise de notas"
// Função : Verificar se a pessoa está aprovada ou não
// Autor :  Carolina
// Data : 18/10/2026
// Seção de Declarações 
var
estudante: caracter
nota1: real
nota2: real
media: real
presencas: inteiro

inicio
// Seção de Comandos
escreval("Digite o nome do(a) estudante")
leia(estudante)

escreval("Insira a primeira nota:")
leia(nota1)

escreval("Insira a segunda nota:")
leia(nota2)

escreval("Qual a frequência do(a) aluno(a):")
leia(presencas)

media <- (nota1+nota2)/2

escreval("Resultado: ",media)

SE(media >=7)E (presencas >=80) ENTAO
escreval("Parabéns, você foi aprovado(a)!")
SENAO
escreval("Infelizmente você foi reprovado(a)!")

FIMSE
fimalgoritmo
