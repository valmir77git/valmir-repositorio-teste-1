# pedir 3 notas e armazenar em variáveis diferentes
nota1 = float (input("digite a nota 1: "))
nota2 = float (input("digite a nota 2: "))
nota3 = float (input("digite a nota 3: "))

soma = nota1 + nota2 + nota3
media = soma/3

print ("A média da nota é",media)

if media >= 7:
    print ("você foi aprovado!")
elif media >= 4:
     print ("você está de recuperação")
else:
     print("Você foi reprovado!")
