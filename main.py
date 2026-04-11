import numpy as np

def criar_mapa(linhas, colunas):
    linhas, colunas = min(linhas, 15), min(colunas, 15)
    total = linhas * colunas
    num_bombas = int(total * 0.3)

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
    while True:
        try:
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            break
        except:
            print("Digite apenas números!\n\n")
    
    mapa = criar_mapa(linhas, colunas)
    imprimir_mapa(mapa)

if __name__ == "__main__":
    main()