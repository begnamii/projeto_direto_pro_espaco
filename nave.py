combustivel = 100
tripulantes = []

def viajar():
    global combustivel
    if len(tripulantes) > 0:
        if combustivel >= 30:
            combustivel = combustivel - 30
            print("\nA nave viajou")
        else:
            print("\nVocê está sem combustível suficiente. Abasteça!")
    else:
        print("\nSem tripulantes suficiente")
    travarMenu()

def abastecer():
    global combustivel
    combustivel = 100
    print("\nTanque cheio!⛽")
    travarMenu()

def status():
    print("\n-------- |Status da Nave| --------")
    print(f"A quantidade de combustível é {combustivel}L")
    print(f"Os tripulantes são: {tripulantes}")
    print("-"*35)
    travarMenu()

def registrarT():
    novoT = input("\nQual o nome do novo tripulante?: ")
    tripulantes.append(novoT)
    print("Tripulante inserido com sucesso! 🚀")
    travarMenu()

def tirarT():
    if len(tripulantes) > 0:
        removido = tripulantes.pop()
        print(f"\n🧑🏼‍🚀 {removido} foi removido da missão")
    else:
        print("\nNinguém a bordo para remover")
    travarMenu()

def travarMenu():
    input("\nPressione <ENTER> para continuar...")

print("\n--- Nave da Bola ---")
print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção: ")
while True:
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Tirar último tripulante | 6- Sair")
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
        tirarT()
    elif(opçao =="6"):
        print("Viagem encerrada!")
        break
        

## lista.pop() Tira o ultimo elemento da lista