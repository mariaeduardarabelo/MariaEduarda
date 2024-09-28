#Estrutura Condicional
print("Calculadora")

numeroUm = float(input("Insira um número:"))
numeroDois = float(input("Insira outro número:"))
operacao = (input("Insira uma operação (+, -, *, /):"))

if operacao == "+":
    print(numeroUm + numeroDois)
elif operacao == "-":
    print(numeroUm - numeroDois)
elif operacao == "*":
    print(numeroUm * numeroDois)
elif operacao == "/":
    if numeroDois == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"{numeroUm} / {numeroDois} = {numeroUm / numeroDois}")
    print(numeroUm / numeroDois)
