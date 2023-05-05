class Item:
    def __init__(self, name: str, price: float, expiration_year: int) -> None:
        self.id: int = None
        self.name: str = name
        self.price: float = price
        self.expiration_year: int = expiration_year

    def is_expired(self) -> bool:
        current_year: int = 2023
        return current_year > self.expiration_year


class Inventory:
    def __init__(self) -> None:
        self.items: list[Item] = []
        self.current_id: int = 0

    def add_item(self, item: Item) -> None:
        item.id = self.current_id
        self.current_id += 1

        self.items.append(item)

    def remove_item(self, item_id: int) -> bool:
        new_items: list[Item] = []
        is_item_removed: bool = False

        for item in self.items:
            if item.id != item_id:
                new_items.append(item)
            else:
                is_item_removed = True

        self.items = new_items
        return is_item_removed

    def display_inventory(self) -> None:
        for item in self.items:
            msg: str = f"Id: {item.id}:  {item.name}"
            print(msg)


class Store:
    def __init__(self, inventory: Inventory) -> None:
        self.inventory: Inventory = inventory

    def check_inventory(self) -> None:
        self.inventory.display_inventory()

    def add_to_inventory(self) -> None:
        item_name: str = input("Enter item name: ")
        item_price: float = float(input("Enter a price: "))
        item_exp_year: int = int(input("Enter item exp year: "))

        item: Item = Item(item_name, item_price, item_exp_year)
        self.inventory.add_item(item)

    def remove_item(self) -> None:
        item_id: int = int(input("Enter an item id: "))
        item_removed: bool = self.inventory.remove_item(item_id)

        if item_removed:
            print("Item was removed successfully")
        else:
            print("No item was found by that id")

        input("Press Enter to Continue")


def main():
    my_inv: Inventory = Inventory()
    my_store: Store = Store(my_inv)

    while True:
        print(
            "\n\n1. Check inventory\n2. Add to inventory\n3. Remove from inventory\n4. Quit\n"
        )

        user_choice: int = int(input("Enter an option: "))

        if user_choice == 1:
            my_store.check_inventory()
        elif user_choice == 2:
            my_store.add_to_inventory()
        elif user_choice == 3:
            my_store.remove_item()
        elif user_choice == 4:
            print("Thanks for shopping with us")
            break


if __name__ == "__main__":
    main()
