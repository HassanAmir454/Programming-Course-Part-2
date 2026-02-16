from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename) # create an object 
rows = inventory_file.read() # read the file from the previous created object
print (f'#####Start : {filename} #####' )
items = []
for row in rows:
    #print(row)
    item = Item.deserialize(row)
    item.display_price()
    items.append(Item.deserialize(row))
print (f'##### {filename} #####' )

while True:
    choice = int(input("Change item value (enter 1 - 4) or 0 to exit: "))
    if choice == 1:
        new_val = input(f"Set new value for {items[0].name}: ")
        new_val = float(new_val)
        items[0].value = new_val
        inventory_file.write(items)
        print("Serializing items into rows.")
        print("#####Rows#####")
        for item in items:
            print(f"{item.name},{item.value},{item.category},{item.weight}")

    elif choice == 2 :
        new_val = input(f"Set new value for {items[1].name}: ")
        new_val = float(new_val)
        items[1].value = new_val
        inventory_file.write(items)
        print("Serializing items into rows.")
        print("#####Rows#####")
        for item in items:
            print(f"{item.name},{item.value},{item.category},{item.weight}")
    elif choice == 3:
        new_val = input(f"Set new value for {items[2].name}: ")
        new_val = float(new_val)
        items[2].value = new_val
        inventory_file.write(items)
        print("Serializing items into rows.")
        print("#####Rows#####")
        for item in items:
            print(f"{item.name},{item.value},{item.category},{item.weight}")
    elif choice == 4:
        new_val = input(f"Set new value for {items[3].name}: ")
        new_val = float(new_val)
        items[3].value = new_val
        inventory_file.write(items)
        print("Serializing items into rows.")
        print("#####Rows#####")
        for item in items:
            print(f"{item.name},{item.value},{item.category},{item.weight}")

    else:
        print("Invalid option selected")
        break

    





