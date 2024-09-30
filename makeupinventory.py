# The code is split into two parts.
# The first part is the class MakeupItem and MakeupInventory and it's various mathods.
# The second part is code for the user to interact and create their inventory.


# ---Part 1. The class MakeupItem and MakeupInventory---

class MakeupItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = int(price)
           
        acceptable_category = ["base", "lips", "eyes", "cheeks", "rare item"]
        if self.category.lower() not in acceptable_category:
            raise ValueError("Category must be 'Base', 'Lips', 'Eyes', 'Cheeks' or 'Rare Item'.") # [1]
            # Here we are ensuring that the input for the category argument are certain values.
            # This is important because items may be organised by category later.
       
    def __str__(self):
        return f"Item Name: {self.name}. Category: {self.category}. Price: {self.price}"
   
   
class MakeupInventory:
    def __init__(self, owner):
            self.owner = owner
            self.inventory = []

    def add_item(self, item):
          self.inventory.append(item)
 
   
    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                return f"{item_name} removed from inventory"
        return f"{item_name} not found in inventory"
   
    def calc_total_cost(self):
        total_cost = sum([item.price for item in self.inventory])
        return total_cost
   
    def get_item_price(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return f"{item_name}: €{item.price}"
        return f"{item_name} not found in inventory"
   
    def group_items(self, group_name):
        grouped_items = []
        for item in self.inventory:
            if item.category.lower() == group_name.lower():
                grouped_items.append(item.name)
        return grouped_items
   
    def inventory_overview(self):
        overview = f"{self.owner} Makeup Inventory:\nTotal items: {len(self.inventory)}\nTotal cost: €{self.calc_total_cost()}\n\n"
        for item in self.inventory:
            overview += str(item) + "\n"
        return overview
         
    def __len__(self):
        return len(self.inventory)
       
    def __str__(self):
        if len(self.inventory) == 0:
            return "Your inventory is empty."
        else:
            return f"{self.owner} Makeup Inventory:\nTotal items: {len(self.inventory)}\nTotal cost: €{self.calc_total_cost()}"
           


# ---Part 2. The user interacting and creating their inventory---

def main():

    # These functions make it easier to make our code more dynamic.
   
    def adding_items():
        print("Enter 'done' when you are finished adding items.")
       
        add_count = 1
        while True:
            item_name = input(f"Add Item {add_count}. Name (e.g 'lipstick') or enter 'done': ")
            if item_name.lower() == 'done':
                break # [2]
            item_cat = input(f"Item {add_count}. Category.\nCategory must be 'Base', 'Lips', 'Eyes', 'Cheeks' or 'Rare Item': ")
            item_price = int(input(f"Item {add_count}. Price (e.g 20): "))
            item = MakeupItem(item_name, item_cat, item_price)
            myinventory.add_item(item) # adding to inventory
            add_count += 1
           
        print(f"{add_count - 1} items successfully added.")
       
   
    def removing_items():
        print("Enter 'done' when you are finished removing items.")
        i_count = 1
        while True:
            item_name = input(f"Remove Item {i_count} or enter 'done': ")
            if item_name.lower() == 'done':
                break
            else:
                message = myinventory.remove_item(item_name)
                print(message)
                i_count += 1
           
        print(f"{i_count - 1} items successfully removed.")

   
    def arranging_by_category():
        while True:
            category = input(f"Enter Category (i.e 'Base', 'Lips', 'Eyes', 'Cheeks' or 'Rare Item') or enter 'done': ").lower()
            if category == 'done':
                break
            items_in_category = myinventory.group_items(category)
            if len(items_in_category) == 0:
                print(f"You have no items in {category}.")
            else:
                print(f"Your items in {category} are: ")
                for item in items_in_category:
                    print(item)

    def getting_price():
        while True:
            item_name = input(f"Enter the item Name or enter 'done': ").lower()
            if item_name == 'done':
                break
            print(myinventory.get_item_price(item_name))
   

    name = input("Enter your name to craete your Makeup Inventory: ")
    myinventory = MakeupInventory(name)
   
    while True:
        next_step = input("Home Menu:\n"
                          "1. Add items to your inventory (Enter 'add')\n"
                          "2. Remove items from your inventory (Enter 'rem')\n"
                          "3. Check you inventory overview SHORT (Enter 'overview s')\n"
                          "4. Check you inventory overview LONG (Enter 'overview l')\n"
                          "5. View items in deferent categories (Enter 'category')\n"
                          "6. View item prices (Enter 'prices')\n"
                          "7. Enter 'done' to EXIT\n\n"
                          "Enter: ").lower()
       
        if next_step == 'done':
            break
        elif next_step == "add":
            adding_items()
        elif next_step == "rem":
            removing_items()
        elif next_step == "overview s":
            print(str(myinventory))
        elif next_step == "overview l":
            print(myinventory.inventory_overview())
        elif next_step == "category":
            arranging_by_category()
        elif next_step == 'prices':
            getting_price()

if __name__ == '__main__':
    main()
