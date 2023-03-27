'''
2) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) – 58
b. Para mulheres: (62.1*h) - 44.7

'''
ident=input("Digite 'H' se você for homem, ou 'M' se for mulher:")

if ident=="H" or "h":
    altura=float(input("Digite sua altura:"))
    peso_ideal=(72.7*altura)-58
    print(f"Seu  peso ideal é {peso_ideal:.2f}kg")

elif ident=="M" or "m":
    altura=float(input("Digite sua altura:"))
    peso_ideal=(62.1*altura)-44.7
    print(f"Seu peso ideal é {peso_ideal:.2f}kg")