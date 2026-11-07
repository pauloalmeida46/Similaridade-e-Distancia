# Exercício 5 — Influência da escala e normalização

import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 22. Crie um DataFrame utilizando pandas.
dados = {
    "Cliente": ["A", "B", "C", "D", "E"],
    "Idade": [20, 25, 40, 55, 70],
    "Renda": [2000, 3000, 6000, 9000, 12000],
}
df = pd.DataFrame(dados).set_index("Cliente")
print("DataFrame original:")
print(df)

# 23. Calcule com math.dist() a distância Euclidiana entre A e B usando os
# valores originais de idade e renda.
distancia_original = math.dist(df.loc["A"], df.loc["B"])
print(f"\nDistância A-B (valores originais): {distancia_original:.4f}")

# 24. Normalize as colunas Idade e Renda utilizando MinMaxScaler, do scikit-learn.
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns,
    index=df.index,
)

# 25. Exiba o DataFrame com os valores normalizados.
print("\nDataFrame normalizado:")
print(df_normalizado)

# 26. Calcule novamente a distância Euclidiana entre A e B usando os valores
# normalizados.
distancia_normalizada = math.dist(
    df_normalizado.loc["A"], df_normalizado.loc["B"]
)
print(f"\nDistância A-B (valores normalizados): {distancia_normalizada:.4f}")

# 27. Compare os dois resultados.
print(
    f"\nComparação: distância original = {distancia_original:.4f} | "
    f"distância normalizada = {distancia_normalizada:.4f}"
)

# A renda possui influência muito maior na distância quando os valores
# originais são utilizados porque sua escala numérica (milhares) é muito
# maior que a da idade (dezenas). Como a distância Euclidiana soma os
# quadrados das diferenças em cada atributo, a diferença de renda domina o
# resultado. Após a normalização (MinMaxScaler), todos os atributos ficam na
# mesma escala (entre 0 e 1), e cada um passa a contribuir de forma
# proporcional e justa para o cálculo da distância.
