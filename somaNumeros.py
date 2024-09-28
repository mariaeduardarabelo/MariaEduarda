
continua = "s"
numeros = []

while continua == "s":
    numero = input("Digite um numero:")
    numeros.append(numero)

    soma = sum(numeros)
    print(soma)


numeroUm = float(input("Insira um número:"))
numeroDois = float(input("Insira outro número:"))
numeroTres = float(input("Insira um número:"))
numeroQuatro = float(input("Insira outro número:"))
numeroCinco = float(input("Insira outro número:"))

resultado = numeroUm + numeroDois+ numeroTres + numeroQuatro + numeroCinco
print(resultado)