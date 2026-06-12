combustivel = 100
tripulantes = []

def viajar():
    global combustivel
    if len(tripulantes) > 0:
        if combustivel >= 30:
            combustivel = combustivel - 30
            print("A nave viajou")
        else:
            print("Você está sem combustível suficiente. Abasteça!")
    else:
        print("Sem tripulantes suficiente")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio!⛽")

def status():
    print("|Status|")
    print(f"A quantidade de combustível é {combustivel}L")
    print(f"Os tripulantes são: {tripulantes}")

def registrarT():
    novoT = input("Qual o nome do novo tripulante?: ")
    tripulantes.append(novoT)
    print("Tripulante inserido com sucesso! 🚀")

def tirarT():
    if len(tripulantes) > 0:
        removido = tripulantes.pop()
        print(f"🧑🏼‍🚀 {removido} foi removido da missão")
    else:
        print("Ninguém a bordo para remover")
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
        if len(tripulantes) == 0:
            print("Nenhum tripulante foi removido porque não há nenhum tripulante")
        else:
            tirarT()
        
    elif(opçao =="6"):
        print("Viagem encerrada!")
        break
        

## lista.pop() Tira o ultimo elemento da lista