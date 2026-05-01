print ("|------------------------|")
print ("|     calculadora        |")
print ("|------------------------|")
print ()
print ("Essa calculadora, faz todas as operções")
print ("a partir de dois números que você informar")
print ()

print ("Digite o valor correspondente ao  cálculo")
print ("que você quer fazer")
print ()
print ("1 - As 4 operações")
print ("2 - Média de 3 valores")
print ("3 - Fóemula de Bháskara")
print ()
opcao = int (input("Digite a opção"))

match opcao:
    case 1:
        first_num = float(input ("Digite o primeiro número: "))
        second_num = float(input("Digite o segundo número: "))
        print ()

                
        adicao = first_num + second_num
        print ("A adição resulta em:",adicao)


        subtracao = first_num - second_num
        print ("A subtração resulta em:subtração")


        multi = first_num * second_num
        print ("A multiplicação resulta em:",multi)

        # Verificando se o segundo número é diferente de 0
        if second_num !=0:
            divisao = first_num / second_num
            print ("A divisão resulta em:",divisao)
        else:
            print ("A divisão não pode ser feita.")
    case 2: 
        print ("Média de 3 valores")
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

    case 3:
     
        print("Fórmula de Bháskara")


print ()

