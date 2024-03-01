#Faça um programa que peça ao usuário para digitar um número inteiro, caso o usuário não digite um número inteiro, informe que não é um número inteiro

# try:
#     num = int(input("Digite um número: "))
#     if num % 2 == 0:
#         print("Esse número é par")
#     else:
#         print("Esse núemro é impar")
# except ValueError:
#     print("Valor digitado não é um inteiro")


#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

# try:
#   hr = int(input("Digite a hora em números inteiros: "))

#   if hr >= 0 and hr <= 11:
#       print("Bom dia")
#   elif hr >= 12 and hr <= 17:
#       print("Boa tarde")
#   elif hr >= 18 and hr <= 23:
#       print("Boa noite")
#   else:
#       print("Horário inválido")
# except:
#    print("Digite apenas números inteiros")

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input("Digite seu primeiro nome: ")
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")