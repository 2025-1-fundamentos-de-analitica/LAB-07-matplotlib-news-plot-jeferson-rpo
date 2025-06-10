"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    os.makedirs("files/plots", exist_ok=True)

    df = pd.read_csv("files/input/news.csv")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Year"], df["Television"], label="Television", color="red", marker="o")
    ax.plot(df["Year"], df["Newspaper"], label="Newspaper", color="blue", marker="v")
    ax.plot(df["Year"], df["Internet"], label="Internet", color="green", marker="s")
    ax.plot(df["Year"], df["Radio"], label="Radio", color="purple", marker="^")

    ax.set_title("Uso de Medios de Información (2001–2010)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Porcentaje")
    ax.legend()
    fig.tight_layout()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.savefig("files/plots/news.png")

    
"""
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

"""
if __name__ == "__main__":
    pregunta_01()