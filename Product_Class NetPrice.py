'''A street hawker is anxious to use his mobile phone for management of his small business. He
only sale the products mentioned below along with their prices. Again, like previous sub task,
you have to provide the self explanatory python example code as answer that how can we use
them.
    Pastry 80, Cream roll 70, Chicken petty 50, Cake rusk 25, French fries 100'''

class product:
    Pastry          = 80
    Cream_roll      = 70
    Chicken_petty   = 50
    Cake_rusk       = 25
    French_fries    = 100

def main():
    print("Enter no of: ")
    p1 = int(input("Pastries = "))
    p2 = int(input("Cream_roll = "))
    p3 = int(input("Chicken_petty = "))
    p4 = int(input("Cake_rusk = "))
    p5 = int(input("French_fries = "))


    pr1 = (product.Pastry) * p1
    pr2 = (product.Cream_roll) * p2
    pr3 = (product.Chicken_petty) * p3
    pr4 = (product.Cake_rusk) * p4
    pr5 = (product.French_fries) * p5
    total = pr1 + pr2 + pr3 + pr4 + pr5
    print("Total =",total)

main()
