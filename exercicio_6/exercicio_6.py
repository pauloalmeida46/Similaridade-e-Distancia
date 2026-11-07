# Exercício 6 — Matriz de distâncias entre registros

import math
import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}

nomes = list(registros.keys())

# 28. Utilize math.dist() para calcular a distância Euclidiana entre todos os
# pares de registros.
# 29. Construa uma matriz de distâncias utilizando pandas.DataFrame.
matriz = pd.DataFrame(index=nomes, columns=nomes, dtype=float)
for nome_1 in nomes:
    for nome_2 in nomes:
        matriz.loc[nome_1, nome_2] = math.dist(registros[nome_1], registros[nome_2])

print("Matriz de distâncias:")
print(matriz)

# 30. Identifique o menor valor diferente de zero.
menor_distancia = None
par_mais_proximo = None
for nome_1 in nomes:
    for nome_2 in nomes:
        distancia = matriz.loc[nome_1, nome_2]
        if distancia > 0 and (menor_distancia is None or distancia < menor_distancia):
            menor_distancia = distancia
            par_mais_proximo = (nome_1, nome_2)

# 31. Informe qual é o par de registros mais próximo.
print(f"\nMenor distância (diferente de zero): {menor_distancia:.4f}")
print(f"Par de registros mais próximo: {par_mais_proximo[0]} e {par_mais_proximo[1]}")

# 32. Verifique que a diagonal principal possui apenas zeros.
# A diagonal é zero porque representa a distância de cada registro para ele
# mesmo, e a distância de um ponto para si mesmo é sempre nula.
diagonal_zerada = all(matriz.loc[nome, nome] == 0 for nome in nomes)
print(f"\nDiagonal principal possui apenas zeros: {diagonal_zerada}")

# 33. Verifique que a matriz é simétrica.
# A matriz é simétrica porque d(A,B) = d(B,A): a distância Euclidiana não
# depende da ordem dos pontos, já que as diferenças são elevadas ao quadrado.
matriz_simetrica = matriz.equals(matriz.T)
print(f"Matriz é simétrica: {matriz_simetrica}")
