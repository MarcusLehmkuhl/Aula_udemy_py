"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite o seu nome:")
idade = input("Digite a sua idade:")
nome_invertido = nome[::-1]
espaco = " "

if espaco in nome:
    tem_espaco = "contém espaço na sua composição"
else:
    tem_espaco = "não contém espaço na sua composição"


if nome or idade == None:
    print(f"Seu nome é {nome}\n Seu nome invertido é {nome_invertido}\n Seu nome {tem_espaco}\n Seu nome contém {len(nome)} letras\n A primeira letra do seu nome é {nome[0:1:]}\n A última letra do seu nome é {nome[-1:]} ")
else:
    #print(f"Seu nome é {nome} \nSeu nome invertido é {nome invertido} \nSeu nome contém (ou não) espaços \nSeu nome tem {n} letras \nA primeira letra do seu nome é {letra} \nA última letra do seu nome é {letra}")
    print("Desculpe, você deixou campos vazios.")