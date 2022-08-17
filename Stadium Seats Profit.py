"""A staduim has three types of seats. A class seats worth 15$,
B class seats worth 12$ and C class seats worth 9$. Calculate the
total income of staduim."""
def income(x, y, z):
    a = x * 15
    b = y * 12
    c = z * 9
    sum = a + b + c 
    return sum



def main():
    A = int(input("Enter the number of seats sold of class A: "))
    B = int(input("Enter the number of seats sold of class B: "))
    C = int(input("Enter the number of seats sold of class C: "))
    
    print("Total income =", income(A,B,C),end="$")



main()