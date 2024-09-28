#Sistema básico de reserva de voos

nomes = []
destinos = []
continua = "s"

while continua == "s":
    nome = input("Digite um nome:")
    nomes.append(nome)

    destino = input("Digite um destino:")
    destinos.append(destino)

    continua = input("Deseja continuar? (s/n): ")
for nome in nomes:
    print("Sistema de Reserva de Voos")
    print(f"Nome: {nome}")
    print(f"Destino: {destino}")
    