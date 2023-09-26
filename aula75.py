# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def multiplicar(num):
#     result2x = num * 2
#     result3x = num * 3
#     result4X = num * 4
#     return f"O numero fornecido 2x = {result2x} 3x = {result3x} 4x = {result4X}"

# print(multiplicar(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))