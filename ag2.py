import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


Tabuleiro = list[list[str]]


def main() -> None:
    df = pd.read_csv("tic-tac-toe.csv", sep=",")

    # Substituindo valores categóricos de entrada por numéricos
    df = df.replace("o", -1).replace("b", 0).replace("x", 1)

    # Substituindo valores categóricos de saída por numéricos
    df = df.replace("negativo", -1).replace("positivo", 1)

    clf = DecisionTreeClassifier()
    x_train, x_test, y_train, y_test = train_test_split(df.drop("resultado", axis=1), df["resultado"], test_size=0.2)

    clf.fit(x_train, y_train)

    accuracy = clf.score(x_test, y_test)

    print(f"Acurácia: {100*accuracy:.2f}%")

    option = input('Caso queira inserir um cenário do jogo da velha, entre com "1": ')
    if option == "1":
        tabuleiro = preencher_jogo_velha()

        data = np.reshape(tabuleiro, (1, 9))
        df2 = pd.DataFrame(data, columns=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        df2 = df2.replace("o", -1).replace("b", 0).replace("x", 1)

        resultado = clf.predict(df2)[0]
        resposta = "SIM" if resultado == 1 else "NÃO"
        print(f"X foi o ganhador: {resposta}!")


def preencher_jogo_velha() -> Tabuleiro:
    print("Entre com o cenário do jogo da velha:")

    tabuleiro = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    for i in range(3):
        for j in range(3):
            print()
            valor = input('Entre com o valor ("o" ou "x"): ')
            tabuleiro[i][j] = valor.lower()
            printar_jogo_velha(tabuleiro)

    return tabuleiro


def printar_jogo_velha(tabuleiro: Tabuleiro) -> None:
    print()
    print(f" {tabuleiro[0][0]:^5} | {tabuleiro[0][1]:^5} | {tabuleiro[0][2]:^5} ")
    print("-"*25)
    print(f" {tabuleiro[1][0]:^5} | {tabuleiro[1][1]:^5} | {tabuleiro[1][2]:^5} ")
    print("-"*25)
    print(f" {tabuleiro[2][0]:^5} | {tabuleiro[2][1]:^5} | {tabuleiro[2][2]:^5} ")
    print()
