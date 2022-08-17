def gpa(a):
    s = [0] * 8
    i = 0
    c = 0
    while i < 8:
        if   a[i] == 'A': s[c] = 4
        elif a[i] == 'B': s[c] = 3
        elif a[i] == 'C': s[c] = 2
        elif a[i] == 'D': s[c] = 1
        else            : s[c] = 0
        i = i + 1
        c = c + 1
    # Calculating gpa
    GPAS = (s[0] * 3) + (s[1] * 1) + (s[2] * 2) + (s[3] * 2) + (s[4] * 1) + (s[5] * 3) + (s[6] * 0.5) + (s[7] * 3)
    GPA = GPAS/15.5
    return GPA

def main():
    a = [0] * 8
    a[0] = input('PF = ')
    a[1] = input('PF Lab = ')
    a[2] = input('PST = ')
    a[3] = input('IICT = ')
    a[4] = input('IICT Lab = ')
    a[5] = input('EEC = ')
    a[6] = input('QT = ')
    a[7] = input('DM = ')
    print(gpa(a))

main()