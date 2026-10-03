print("Parking fee for the vehicles per hour are as follows:")

print("Choose 1 for Bike : Rs 20")
print("Choose 2 for Car : Rs 40")
print("Choose 3 for Truck : Rs 100")

a = int(input("Enter your choice : "))
b = int(input("Enter no. of hours : "))
if a == 1:
    print("Amount : ", 20*b)
elif a == 2:
    print("Amount : ", 40*b)
elif a == 3:
    print("Amount : ", 100*b)
else:
    print("Invalid")

