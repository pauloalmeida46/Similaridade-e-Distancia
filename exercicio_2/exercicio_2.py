# Exercício 2 — Qual cliente é mais semelhante ao cliente A?
# Restrição: não utilizar funções prontas de distância.

cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]


def distancia_euclidiana(p1, p2):
    diferenca_idade = p1[0] - p2[0]
    diferenca_compras = p1[1] - p2[1]
    soma_quadrados = diferenca_idade ** 2 + diferenca_compras ** 2
    return soma_quadrados ** 0.5


# 8. Calcule manualmente a distância Euclidiana entre A e B.
distancia_ab = distancia_euclidiana(cliente_a, cliente_b)

# 9. Calcule manualmente a distância Euclidiana entre A e C.
distancia_ac = distancia_euclidiana(cliente_a, cliente_c)

# 10. Calcule manualmente a distância Euclidiana entre A e D.
distancia_ad = distancia_euclidiana(cliente_a, cliente_d)

# 11. Compare os três resultados.
distancias = {"B": distancia_ab, "C": distancia_ac, "D": distancia_ad}

# 12. Determine qual cliente possui a menor distância em relação ao cliente A.
cliente_mais_proximo = min(distancias, key=distancias.get)

# 13. Exiba todas as distâncias e o cliente mais próximo.
print(f"Distância A-B: {distancia_ab:.4f}")
print(f"Distância A-C: {distancia_ac:.4f}")
print(f"Distância A-D: {distancia_ad:.4f}")
print(f"Cliente mais próximo de A: {cliente_mais_proximo}")

# A menor distância indica maior semelhança porque a distância Euclidiana mede
# o quão "distantes" dois pontos estão no espaço formado pelos atributos
# (idade e compras por mês): quanto menores as diferenças em cada atributo,
# menor a distância resultante, logo mais parecidos são os perfis comparados.
