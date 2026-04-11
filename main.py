import numpy as np

def criar_mapa(linhas, colunas):
    linhas, colunas = min(linhas, 15), min(colunas, 15)
    total = linhas * colunas
    num_bombas = int(total * 0.25)

    mapa = np.full((linhas, colunas), '-')

    posicoes = np.random.choice(total, num_bombas, replace=False)
    for pos in posicoes:
        linha = pos // colunas
        coluna = pos % colunas
        mapa[linha][coluna] = '*'

    return calcular_numeros(mapa)

def calcular_numeros(mapa):
    linhas, colunas = mapa.shape
    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == '*':
                continue
            bombas_adjacentes = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < linhas and 0 <= nj < colunas and mapa[ni][nj] == '*':
                        bombas_adjacentes += 1
            if bombas_adjacentes > 0:
                mapa[i][j] = str(bombas_adjacentes)
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