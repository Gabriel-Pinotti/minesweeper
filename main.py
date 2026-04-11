import numpy as np

def criar_mapa(linhas, colunas):
    total = linhas * colunas
    num_bombas = int(total * 0.25)

    mapa = np.full((linhas, colunas), '-')

    posicoes = np.random.choice(total, num_bombas, replace=False)
    for pos in posicoes:
        linha = pos // colunas
        coluna = pos % colunas
        mapa[linha][coluna] = '*'

    return mapa

def imprimir_mapa(mapa):
    for linha in mapa:
        print(' '.join(linha))

def main():
    print("=== Campo Minado ===")
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))

    mapa = criar_mapa(linhas, colunas)
    imprimir_mapa(mapa)

if __name__ == "__main__":
    main()