st = 1
sp = 2
n = sp
for row in range(2, 6):
    for col in range (st, sp):
        n -=1
        print(n, end=' ')
    print("")
    st = sp
    sp += row
    n = sp