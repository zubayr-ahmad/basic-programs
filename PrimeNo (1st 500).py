def IsPrime(n):
    i = 2
    a = True
    while i < n:
        if n%i==0:
            a = False
        i = i + 1
    return a
def main():
    n = 2
    i = 1
    while i <= 500:
        if IsPrime(n) == True:
            print(n)
            i = i + 1
        n = n + 1

main()