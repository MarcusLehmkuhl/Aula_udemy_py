primeiro_numero = input("Digite o primeiro número:")
operador = input("Qual o sinal será usado")
segundo_numero = input("Digite o segundo número:")


resultado = 0

if operador == "+":
    resultado = float(primeiro_numero) + float(segundo_numero)
    print(resultado)
elif operador == "-":
    resultado = float(primeiro_numero) - float(segundo_numero)
    print(resultado)
elif operador == "*":
    resultado = float(primeiro_numero) * float(segundo_numero)
    print(resultado)
elif operador == "/":
    resultado = float(primeiro_numero) / float(segundo_numero)
    print(resultado)
else:
    None == primeiro_numero and segundo_numero 
    print("Você deve colocar um número")

    
