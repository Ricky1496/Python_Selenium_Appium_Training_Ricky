class Item:
    # id = None  # static or class of the variable
    # descr = None
    # quantity = None
    # price = None

    def __int__(self):
        self.id = None  #
        self.descr = None
        self.quantity = None
        self.price = None

    def print_data(self):
        print(self.id)
        print(self.descr)
        print(self.quantity)
        print(self.price)

    def discount(self):
        if self.quantity == 2:
            self.quantity = self.price - (self.price * (10/100)) #price minus discount
            print (self.quantity)
        elif self.quantity >=3 and self.quantity <=5:
            self.quantity = self.price - (self.price * (15 / 100))  # price minus discount
            print(self.quantity)