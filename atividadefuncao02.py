# Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre eles.

def negosio():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    soma = numero1 + numero2
    subtracao1 = numero1 - numero2
    subtracao2 = numero2 - numero1
    multiplicacao = numero1 * numero2
    divisao1 = numero1 / numero2
    divisao2 = numero2 / numero1
    print("A soma entre os dois números é: ", soma)
    print("A subtração do primeiro número pelo segundo número é: ", subtracao1)
    print("A subtração do segundo número pelo primeiro número é: ", subtracao2)
    print("A multiplicação do primeiro número pelo segundo (e virse-versa) é: ", multiplicacao)
    print("A divisão do primeiro número pelo segundo número é igual a: ", divisao1)
    print("A divisão do segundo número pelo primeiro número é igual a: ", divisao2)

negosio()