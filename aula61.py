"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
      #012345678910

cpf = "746.824.890-70"
r0 = int(cpf[0]) * 10 
r1 = int(cpf[1]) * 9
r2 = int(cpf[2]) * 8 
r3 = int(cpf[4]) * 7 
r4 = int(cpf[5]) * 6 
r5 = int(cpf[6]) * 5 
r6 = int(cpf[8]) * 4 
r7 = int(cpf[9]) * 3 
r8 = int(cpf[10]) * 2
result_soma_div = r0+r1+r2+r3+r4+r5+r6+r7+r8
resultado_final = result_soma_div * 10
result_resto_div = resultado_final % 11
if result_resto_div > 9:
    final_num = 0
else:
    final_num = result_resto_div
print(f"O primeiro dígito do CPF é ", result_resto_div)