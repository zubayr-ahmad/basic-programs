w = float(input("Enter weight (in pounds): "))
h = float(input("Enter height (in inches): "))
def BMI(w,h):
    B = (w * 703)/(h*h)
    return B
print(BMI(w,h))