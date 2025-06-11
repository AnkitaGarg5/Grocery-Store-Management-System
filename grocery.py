grocery_items={}
def add_item():
    name=input("Enter item name: ")
    price=float(input("Enter price per unit: "))
    quantity=int(input("Enter quantity:"))
    if name in grocery_items:
        grocery_items[name]["quantity"]+=quantity
    else:
        grocery_items[name]={"price":price ,"quantity":quantity}
    print(f"{quantity} {name} (s) added to inventory.")

def view_items():
    if not grocery_items:
        print("Inventory is empty")
        return
    print("\nCurrent Inventory:")
    print("{:<15} {:<10} {:<10}".format("Item","Price","Quantity"))
    for item,info in grocery_items.items():# grocery_items is a dictionary . .items()->gives you all items in the dictionary as key value pairs
        
        print("{:<15} {:<10} {:<10}".format(item,info['price'],info['quantity']))
        #info['price']->the price of one unit
        #info['quantity']->how many units are in stock

def generate_bill():
    total=0
    print("\n----Bill---")
    for item ,info in grocery_items.items():
        item_total=info['price']*info['quantity']#cost of that item
        print(f"{item}: {info['quantity']} X {info['price']}={item_total}")#show each item in the bill with its price calculation
        total+=item_total
        print(f"Total Amount:Rs{total}")

def main():#main program
    while True:
        print("\n===Grocery Store Menu===")
        print("1.Add item")
        print("2.View Inventory")
        print("3.Generate Bill")
        print("4.Exit")
        choice=input("Enter your choice(1-4): ")
        if choice=='1':
            add_item()
        elif choice=='2':
            view_items()
        elif choice=='3':
            generate_bill()
        elif choice=='4':
            print("Thank you for using Grocery store Management System")
            break
        else:
            print("Invalid choice")
if __name__=="__main__":#if you run file start by calling main function
    main()
    











