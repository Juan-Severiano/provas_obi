M, N = map(int, input().split())
estoque = []
for i in range(M):
    linha = list(map(int, input().split()))
    for quantidade in linha:
        if quantidade < 0:
            print("Valores de estoque inválidos.")
            exit()
    estoque.append(linha)

vendas = 0
P = int(input())

for i in range(P):
    I, J = map(int, input().split())
    if not (1 <= I <= M) or not (1 <= J <= N):
        print("Pedido inválido.")
        exit()

    if estoque[I-1][J-1] > 0:
        estoque[I-1][J-1] -= 1
        vendas += 1

print(vendas)
