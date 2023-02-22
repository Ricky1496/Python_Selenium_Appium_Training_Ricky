from item_package.item_module import Item

class ShoppingCart:

    item_1 = Item()
    item_2 = Item()

    item_1.descr("Cosmic byte Cooling Fan")
    item_2.descr("Razor gaming mouse")

    print(item_1.descr)
    print(item_2.descr)