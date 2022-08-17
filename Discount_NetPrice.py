"""Write a program that calculates the total cost after shoping.
The price of a package is 99$. If a person buy at least 10 packages then
he will get 20% discount. From 20 packages onwards, 30% discount is 
available. from 50 to 99, it is 40% discount and for more than 100 
packages, 50% discount is available."""
one_package = 99
discount = 0
packages = int(input("Enter the number of packages purchases: "))
if (packages >= 10) and (packages <= 19):
    b = 0.2
elif (packages >= 20) and (packages < 50):
    b = 0.3
elif (packages >= 50) and (packages < 100):
    b = 0.4
elif (packages >= 100):
    b = 0.5
actual_price = one_package * packages
discounted_price = actual_price * discount
total_price = actual_price - discounted_price
if packages < 10:
    print("Price =",actual_price, end="$")
else:
    print("Price =",total_price, end="$")
