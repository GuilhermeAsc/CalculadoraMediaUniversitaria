# Calculadora de média escolar
# By asC-_

def mediax(x,y):
    calcularmedia = (x+y)/2
    return calcularmedia

a =  0

while( a != 'fim'):
    nome  = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    matricula = int(input("Digite sua matrícula: "))
    ano_de_curso = int(input("Digite seu ano de curso: "))
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    if nota1 > 10:
        print("Por favor digite uma nota que seja entre 0 e 10!!")
        break
    elif nota2 > 10:
        print("Por favor digite uma nota entre 0 e 10")
        break
    media = mediax(nota1,nota2)
    print(mediax(nota1,nota2))

    if media >= 6:
        print("Aluno aprovado")
    elif media <=3 :
        print("Reprovado")
    if input('para sair digite (f) para continuar (enter): ') == 'f':
       break