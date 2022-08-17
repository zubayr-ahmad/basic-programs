# Restaurant slip

def tip(charge):
    tip = charge * (0.15)
    return round(tip,2)


def salesTax(charge):
    sales_tax = charge * (0.07)
    return round(sales_tax,2)


def main():
    charge = int(input("Enter the actual cost for food: "))
    x1 = tip(charge)
    x2 = salesTax(charge)
    print("Charge of food =", charge)
    print("Tip =", x1)
    print("Sales Tax =", x2)
    total = charge + x1 + x2
    print("Total =", round(total,2))
    print("Thanks for your visit!")


main()
