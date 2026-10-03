a = int(input("Enter no. of items: "))
total = 0
shop = {}
for i in range(a):
    item = str(input("Product name: "))
    price = int(input("Price: "))
    shop[item] = price
    total = total + price
print("Products list")
print(shop)
if total >= 500 and total< 1000:
    
    print("Total Amount: ", total)
    total =  total - (total/10)
    print("Total after 10% discount: ", total)
elif total >= 1000:

    print("Total Amount: ", total)
    total =  total - (total/5)
    print("Total after 20% discount: ", total)
else:
    print("Total Amount: ", total)


