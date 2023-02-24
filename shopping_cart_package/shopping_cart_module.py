from item_package.item_module import Item

if __name__ == "__main__":

    item1 = Item()
    item2 = Item()

    item1.id = 1001
    item1.descr = "apple"
    item1.quantity = 2
    item1.price = 30

    item2.id = 1002
    item2.descr = "glass"
    item2.quantity = 5
    item2.price = 20

    item1.print_data()
    item2.print_data()