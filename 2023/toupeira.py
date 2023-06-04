def dfs(salao_atual, destino, visitados, adjacencias):
    visitados[salao_atual] = True

    if salao_atual == destino:
        return True

    for salao_vizinho in adjacencias[salao_atual]:
        if not visitados[salao_vizinho]:
            if dfs(salao_vizinho, destino, visitados, adjacencias):
                return True

    return False


def verifica_passeios(s, t, adjacencias, passeios):
    total_possiveis = 0

    for passeio in passeios:
        possivel = True
        n = len(passeio)

        for i in range(n - 1):
            origem = passeio[i]
            destino = passeio[i + 1]

            visitados = [False] * (s + 1)
            visitados[origem] = True

            if not dfs(origem, destino, visitados, adjacencias):
                possivel = False
                break

        if possivel:
            total_possiveis += 1

    return total_possiveis


s, t = map(int, input().split())

adjacencias = [[] for _ in range(s + 1)]

for _ in range(t):
    x, y = map(int, input().split())
    adjacencias[x].append(y)
    adjacencias[y].append(x)

p = int(input())

passeios = []
for _ in range(p):
    passeio = list(map(int, input().split()))[1:]
    passeios.append(passeio)

total_possiveis = verifica_passeios(s, t, adjacencias, passeios)

print(total_possiveis)
