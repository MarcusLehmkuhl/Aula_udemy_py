
"""primeiro_num = int(input("Digite o primeiro número a ser computado:"))
segundo_num = int(input("Digite o segundo número a ser computado:"))
operacao = input("Escolha um operador '+' '-' '/' '*' :")

if operacao == "+":
    resultado = primeiro_num + segundo_num
    print(resultado)
elif operacao == "-":
    resultado = primeiro_num - segundo_num
    print(resultado) 
elif operacao == "/":
    resultado = primeiro_num / segundo_num
    print(resultado)
elif operacao == "*":
    resultado = primeiro_num * segundo_num
    print(resultado)"""

# Calculadora While

""" Calculadora com while """
bloco_1 = True
while bloco_1 == True:
    operador_1 = input("Digite o primeiro número a ser operado:")
    operador_2 = input("Digite o segundo número a ser operado:")
    sinal_operador = input("Digite [+] para somar, [-] para subtrair, [*] para multiplicar e [/] para dividir:") 
    if sinal_operador == "+":
        resultado = float(operador_1) + float(operador_2)
        print(f"O resutado final é {resultado}")
        bloco_1 = False
    elif sinal_operador == "-":
        resultado = float(operador_1) - float(operador_2)
        print(f"O resutado final é {resultado}")
        bloco_1 = False
    elif sinal_operador == "*":
        resultado = float(operador_1) * float(operador_2)
        print(f"O resutado final é {resultado}")
        bloco_1 = False
    elif sinal_operador == "/":
        resultado = float(operador_1) / float(operador_2)
        print(f"O resutado final é {resultado}")
        bloco_1 = False
    else:
        print("Algo deu errado!\n Repita o processo.")
        continue
        
        
