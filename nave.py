combustivel = 100
tripulantes = []

def viajar():
    global combustivel
    if combustivel >= 30:
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustível suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio!⛽")

def status():
    print(f"A quantidade de combustível é {combustivel}L")
    print(f"Os tripulantes são: {tripulantes}")

def registrarT():
    novoT = input("Qual o nome do novo tripulante?: ")
    tripulantes.append(novoT)
    print("Tripulante inserido com sucesso! 🚀")

print("\n--- Nave da Bola ---")
print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção: ")
while True:
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Sair")
    opçao = input("Escolha: ")
    if (opçao == "1"):
        status()
    elif (opçao == "2"):
        viajar()
    elif(opçao == "3"):
        abastecer()
    elif(opçao == "4"):
        registrarT()
    elif(opçao == "5"):
        print("Viagem encerrada!")
        break