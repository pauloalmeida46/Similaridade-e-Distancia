# Exercício 3 — Distância Euclidiana com três atributos
# Restrição: não utilizar funções prontas de distância.

aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana(p1, p2):
    soma_quadrados = 0
    for i in range(len(p1)):
        diferenca = p1[i] - p2[i]
        soma_quadrados += diferenca ** 2
    return soma_quadrados ** 0.5


# 14. Implemente manualmente a distância Euclidiana entre A e B.
distancia_ab = distancia_euclidiana(aluno_a, aluno_b)

# 15. Implemente manualmente a distância Euclidiana entre A e C.
distancia_ac = distancia_euclidiana(aluno_a, aluno_c)

# 16. Exiba os dois resultados.
print(f"Distância A-B: {distancia_ab:.4f}")
print(f"Distância A-C: {distancia_ac:.4f}")

# 17. Informe qual aluno está mais próximo de A.
if distancia_ab < distancia_ac:
    print("Aluno mais próximo de A: B")
else:
    print("Aluno mais próximo de A: C")

# A mesma lógica usada em duas dimensões (somar as diferenças ao quadrado de
# cada atributo e tirar a raiz quadrada) se generaliza para qualquer número
# de atributos, bastando somar o quadrado da diferença de cada dimensão.
