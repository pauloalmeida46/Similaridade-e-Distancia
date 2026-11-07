# Exercício 4 — Comparando vários clientes com math.dist()

# 18. Importe o módulo math.
import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}

referencia = clientes["A"]

# 19. Utilize math.dist() para calcular a distância de A para B, C, D e E.
distancias = {}
for nome, atributos in clientes.items():
    if nome == "A":
        continue
    distancias[nome] = math.dist(referencia, atributos)

# 20. Exiba cada distância calculada.
for nome, distancia in distancias.items():
    print(f"Distância A-{nome}: {distancia:.4f}")

# 21. Identifique automaticamente o cliente mais próximo de A.
cliente_mais_proximo = min(distancias, key=distancias.get)

# Ao final: frase informando qual cliente possui o perfil mais próximo de A.
print(
    f"O cliente com perfil mais próximo de A, considerando idade e compras "
    f"por mês, é o cliente {cliente_mais_proximo}."
)
