# Exercício 1 — Distância Euclidiana entre dois clientes
# Restrição: não utilizar math.dist() nem qualquer função pronta para cálculo de distância.

# 1. Armazene os dados dos clientes em listas.
cliente_a = [25, 2]
cliente_b = [28, 6]

# 2. Calcule a diferença entre as idades.
diferenca_idade = cliente_a[0] - cliente_b[0]

# 3. Calcule a diferença entre as quantidades de compras.
diferenca_compras = cliente_a[1] - cliente_b[1]

# 4. Eleve cada diferença ao quadrado.
quadrado_idade = diferenca_idade ** 2
quadrado_compras = diferenca_compras ** 2

# 5. Some os resultados obtidos.
soma_quadrados = quadrado_idade + quadrado_compras

# 6. Calcule a raiz quadrada da soma.
distancia_euclidiana = soma_quadrados ** 0.5

# 7. Exiba a distância Euclidiana entre os dois clientes.
print(f"Distância Euclidiana entre o cliente A e o cliente B: {distancia_euclidiana:.4f}")
