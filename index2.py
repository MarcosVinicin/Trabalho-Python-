comida = ["Hamburguer","Pizza","Misto","Salada"]
bebida = ["Refrigerante", "Suco", "Àgua"]

def comer():
    print("0- Hamburguer \n 1- Pizza \n 2- Misto \n 3- Salada\n Qual dessas opções voce quer pedir? ")

def responder():
    print("Voce gosta de " +comida[posicao]+ " acompanhado de alguma bebida? sim/não")

def beber():
    print("0- Refrigerante \n 1- Suco \n 2- Àgua \n Qual bebida voce quer? ")

def pedido_bebida():
    print("Seu pedido com "+comida[posicao]+" e "+bebida[escolha_bebida]+" já está sendo preparado")
    
def pedido():
    print("Seu pedido de "+comida[posicao]+" já está sendo preparado! Obrigado!")

comer()
opcoes=input()

posicao = int(opcoes)

if posicao==0:
    responder()
    escolha=input()
    if escolha.lower()=="sim":
        beber()
        escolha2=input()
        escolha_bebida=int(escolha2)
        pedido_bebida()
    else:
        pedido()

if posicao==1:
    responder()
    escolha=input()
    if escolha.lower()=="sim":
        beber()
        escolha2=input()
        escolha_bebida=int(escolha2)
        pedido_bebida()
    else:
        pedido()

if posicao==2:
    responder()
    escolha=input()
    if escolha.lower()=="sim":
        beber()
        escolha2=input()
        escolha_bebida=int(escolha2)
        pedido_bebida()
    else:
        pedido()

if posicao==3:
    responder()
    escolha=input()
    if escolha.lower()=="sim":
        beber()
        escolha2=input()
        escolha_bebida=int(escolha2)
        pedido_bebida()
    else:
        pedido()



