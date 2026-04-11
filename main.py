import numpy as np

def criar_mapa(linhas, colunas):
    return np.full((linhas, colunas), '-')

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