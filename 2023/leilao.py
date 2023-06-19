n = int(input())


max_lance = 0
winner_name = ""

if 0 <= n <= 10000:
    for i in range(n):
        name = input()
        value = int(input())

        if 1 <= value <= 100000 and 1 <= len(name) <= 10:
            if value > max_lance:
                max_lance = value
                winner_name = name
        else:
            print('invalid')
else:
    print('invalid')


print(winner_name)
print(max_lance)