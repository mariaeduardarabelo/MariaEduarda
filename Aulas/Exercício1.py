# Atividade 1 
# Existe um calculo que faz a correção do peso e altura de um individuo, o IMC (índice de massa corporal). Para calcular o IMC de uma pessoa devemos saber sua altura, seu peso e aplicar a formula "IMC = Peso / altura²;
# Crie um programa que solicite o nome, peso e altura de uma pessoa. Ao final saúde a pessoa e mostre o resultado do IMC.

nome = (input("Qual o seu nome?"))
print(f"Olá, {nome}!")
peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))
imc = peso/altura**2
print(f"Seu peso:{peso}")
print(f"Sua altura:{altura}")
print(f"Seu imc é:{imc:.2f}")
