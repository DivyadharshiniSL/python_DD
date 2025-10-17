items=[]
price_items=[]
num_items= int(input("how many items?"))
for i in range(num_items):
    items_name= input(f"Name of the item{i+1}:")
    items_price=int(input(f"price of the item:"))
    items.append(items_name) 
    price_items.append(items_price)
print("\n----Items list----")
for i in range(len(items_name)):
    print(f"{items_name[i]} - {items_price[i]} Rs")
highest=max(items_price)
lowest=min(items_price)
average=sum(items_price)/len(items_price)
print("\n---Statistics---")
print("Highest price:",highest)
print("Lowest price:",lowest)
print("Average:",average)
