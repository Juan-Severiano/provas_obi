v = int(input())
a = int(input())
f = int(input())
p = int(input())

contas_pagas = 0
if 0 <= v <= 2000 and 1 <= a <= 1000 and 1 <= f <= 1000 and 1 <= p <= 1000:
    if v >= a:
        v -= a
        contas_pagas += 1

    if v >= f :
        v -= f
        contas_pagas += 1

    if v >= p :
        v -= p
        contas_pagas += 1


    print(contas_pagas)
else:
    print('valores invalidos')

