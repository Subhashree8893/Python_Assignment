# Referal Id - SIRSS2335
# Name - Subhashree Sahu
def print_pascaltriangle(size):
    for i in range(0, size):
        for j in range(0, i+1):
            print(number(i, j), end=" ")
        print()
def number(n, k):
    no =1
    if k> n - k:
        k = n - k
    for i in range(0, k):
        no = no * (n - i)
        no = no // (i + 1)
    return no
rows = 7
print_pascaltriangle(rows)        
