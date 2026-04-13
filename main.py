import numpy as np

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

def carregar_mapa(caminho='mapa.txt'):
    with open(caminho, 'r') as f:
        linhas, colunas = map(int, f.readline().split())
        mapa = np.full((linhas, colunas), '-')
        for linha in f:
            i, j = map(int, linha.split())
            numpy_linha = linhas - j
            numpy_coluna = i - 1
            mapa[numpy_linha][numpy_coluna] = '*'
    return calcular_numeros(mapa)

def criar_mapa_visivel(linhas, colunas):
    return np.full((linhas, colunas), '#')

def imprimir_mapa(mapa):
    for linha in mapa:
        print(' '.join(linha))

def parsear_coordenada(entrada, linhas, colunas):
    try:
        entrada = entrada.strip().lower()
        coluna = ord(entrada[0]) - ord('a')
        linha = linhas - int(entrada[1:])
        if 0 <= linha < linhas and 0 <= coluna < colunas:
            return linha, coluna
        return None
    except:
        return None

def revelar(mapa_real, mapa_visivel, linha, coluna):
    celula = mapa_real[linha][coluna]

    if celula == '*':
        mapa_visivel[linha][coluna] = '*'
        return 'game_over'

    mapa_visivel[linha][coluna] = celula

    if celula == '-':
        linhas, colunas = mapa_real.shape
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = linha + di, coluna + dj
                if 0 <= ni < linhas and 0 <= nj < colunas and mapa_visivel[ni][nj] == '#':
                    mapa_visivel[ni][nj] = mapa_real[ni][nj]

    return 'ok'

def checar_vitoria(mapa_real, mapa_visivel):
    return np.sum(mapa_visivel == '#') == np.sum(mapa_real == '*')

def main():
    print("=== Campo Minado ===")
    try:
        mapa_real = carregar_mapa()
    except FileNotFoundError:
        print("Arquivo mapa.txt não encontrado!")
        return

    mapa_visivel = criar_mapa_visivel(*mapa_real.shape)
    print("\nLetras: colunas\nNúmeros: linhas\n")

    while True:
        imprimir_mapa(mapa_visivel)
        
        try:
            entrada = input("\nDigite uma coordenada: ")
        except:
            print("Entrada inválida!\n")
            continue

        coordenada = parsear_coordenada(entrada, *mapa_real.shape)
        if coordenada is None:
            print("Coordenada inválida!")
            continue

        linha, coluna = coordenada
        resultado = revelar(mapa_real, mapa_visivel, linha, coluna)

        if resultado == 'game_over':
            imprimir_mapa(mapa_visivel)
            print("\nBOOM! Fim de jogo")
            break

        if checar_vitoria(mapa_real, mapa_visivel):
            imprimir_mapa(mapa_visivel)
            print("\nVocê venceu!")
            break

if __name__ == "__main__":
    main()