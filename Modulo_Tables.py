def modulo_Add(a):
    print('Modulo table w.r.t Addition')

    l = len(a)
    j = 0
    max = a[j]
    while j < len(a):
        if a[j] > max:
            max = a[j]
        j += 1              # Findig greatest value for taking modulo

    i = 0
    print('+', end='\t')
    while i < l:         # First line of the Table
        print(a[i], end='\t')
        i += 1
    print()
    i = 0       # nth column number
    q = 0       # rth row element
    while i < l:
        q = 0
        print(a[i], end='\t')    # Printing first column
        while q < l:
            print((a[i] + a[q]) % max, end='\t')
            q = q + 1
        print()
        i = i + 1


def modulo_Multiply(a):
    print('Modulo table w.r.t Multiplication')
    l = len(a)
    j = 0
    max = a[j]
    while j < len(a):
        if a[j] > max:
            max = a[j]
        j += 1              # Findig greatest value for taking modulo

    i = 0
    print('*', end='\t')
    while i < l:         # First line of the Table
        print(a[i], end='\t')
        i += 1
    print()
    i = 0       # nth column number
    q = 0       # rth row element
    while i < l:
        q = 0
        print(a[i], end='\t')    # Printing first column
        while q < l:
            print((a[i] * a[q]) % max, end='\t')
            q = q + 1
        print()
        i = i + 1


def main():
    numbers_length = int(
        input("How many numbers you want to use in modulo table: "))
    print("Enter numbers")
    numbers = []
    for i in range(numbers_length):
        a = int(input())
        numbers.append(a)
    
    
    print(modulo_Add(numbers)) # Find the difference and reason of the two tables.
    print()
    modulo_Multiply(numbers)


main()
