nota = int(input("Insira sua nota de 0 a 100:"))

if nota <= 60:
    print("Nota F")
elif nota <= 69:
    print("Nota D")
elif nota <= 79:
    print("Nota C")
elif nota <= 89:
    print("Nota B")
elif nota <= 100:
    print("Nota A")
else:
    print("Nota inválida")