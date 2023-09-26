'''tipo_de_calculo = input("Você quer somar, multiplicar, dividir ou subtrair?")
entrada1 = float(input("Digite o primeiro número"))
entrada2 = float(input("Digite o segundo número"))

if tipo_de_calculo == "somar":
    resultado = entrada1 + entrada2
    print(f"O resuntado da sua soma é de {resultado} ")
elif tipo_de_calculo == "multiplicar":
    resultado = entrada1 * entrada2
    print(f"O resuntado da sua multiplicação é {resultado}")
elif tipo_de_calculo == "dividir":
    resultado = entrada1 / entrada2
    print(f"O resuntado da sua divisão é de {resultado}")
elif tipo_de_calculo == "subtrair":
    resultado = entrada1 - entrada2
    print(f"O resuntado da sua subtração é de {resultado}")
else:
    print(f"Você deve selecionar um tipo de calculo")'''

primeiro_valor = input("Digite um valor:")
segundo_valor = input("Digite outro valor:")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor = '{primeiro_valor}' é maior que o segundo valor = '{segundo_valor}'")
elif primeiro_valor < segundo_valor:
    print(f"O segundo valor = '{segundo_valor}' é maior que o primeiro valor = '{primeiro_valor}'")
elif primeiro_valor == segundo_valor:
    print("Os valores são os mesmos")
