'''
-Create one class named “location” with members “name”, “code”.
-Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
-Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. This method will return all “movement” objects which belong to the passed “product” as an argument.
-Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
-Create 4 different location objects.
-Create 5 different product objects.
-Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve.
-Display movements of each product using the “movement_by_product” method.
-Display product details with its stock at various locations using “stock_at_locations”.
-Display product list by location ( group by location).
'''



class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return self.name

    # Display product list by location ( group by location)
    @staticmethod
    def sort(l_list):
        for loc in range(len(l_list)):
            for loc1 in range(loc + 1, len(l_list)):
                if l_list[loc].name > l_list[loc1].name:
                    l_list[loc], l_list[loc1] = l_list[loc1], l_list[loc]
        for loc in l_list:
            print("Location name:", loc.name)
            for product1 in mov_list:
                if loc == product1.from_location:
                    print("Product details :", "Name :", product1.product.name, '|', "Code :", product1.product.code,
                          '|', "Price :", product1.product.price, '|', "Stock of products :",
                          product1.product.stock_at_locations)
            print()

    def show_location(self):
        print("Location name : ", self.name, '\n', "Code : ", self.code)


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.change_value()
        product.stock_at_locations.update({str(self.to_location.name): str(self.quantity)})
        # product.stock_at_locations.update({str(self.from_location): str(self.stock())})

    def change_value(self):
        for i, j in self.product.stock_at_locations.items():
            self.product.stock_at_locations[i] = j - self.quantity
            # raise Exception("Out of stock")
            # if self.quantity <= j:
            #     self.product.stock_at_locations[i] = j - self.quantity
            #     print(self.product.stock_at_locations[i])
            # else:
            #     raise Exception("Out of stock")

    # Display movements of each product using the “movement_by_product” method
    @staticmethod
    def movements_by_product(product):
        for pro in mov_list:
            if pro.product == product:
                pro.show_movement()

    def show_movement(self):
        print("From location : ", self.from_location.name, " ", "To ", self.to_location.name, '|',
              "Product :", self.product.name, '|', "Quantity :", str(self.quantity))


class Product:
    def __init__(self, name, code, price, stock_at_locations):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = stock_at_locations

    def show_product(self):
        return print("Product name :", self.name, '|', "Code :", str(self.code), '|',
                     "Price :", str(self.price), '|', "Stock at locations :", self.stock_at_locations)


# Create location class object
rajkot = Location("Rajkot", 101)
jamnagar = Location("Gandhinagar", 102)
ahmadabad = Location("Baroda", 103)
baroda = Location("Ahmadabad", 104)

# Create product class object
Tv = Product("Tv", 201, 50000, {Baroda: 30})
Laptop = Product("Laptop", 202, 45000, {Rajkot: 40})
Mobile = Product("Mobile", 203, 30000, {Gandhinagar: 50})
Smart watch = Product("Smart watch", 204, 20000, {Rajkot: 60})
Earbuds = Product("Earbuds", 205, 5000, {Ahmadabad: 80})

# Create movement class object
m1 = Movement(Baroda, ahmadabad, Tv, 20)
m2 = Movement(Rajkot, baroda, Laptop, 35)
m3 = Movement(Gandhinagar, Ahmadabad, Mobile, 25)
m4 = Movement(Rajkot, Gandhinagar, Smart watch, 50)
m5 = Movement(Ahmadabad, Rajkot, Earbuds, 63)

print()
print(".....Display movements of each product using the movement_by_product method.....")
mov_list = [m1, m2, m3, m4, m5]
Movement.movements_by_product(Tv)
Movement.movements_by_product(Laptop)
Movement.movements_by_product(Mobile)
Movement.movements_by_product(Smart watch)
Movement.movements_by_product(Earbuds)

print()
print(".....Display product details with its stock at various locations using stock_at_locations.....")
Tv.show_product()
Laptop.show_product()
Mobile.show_product()
Smart watch.show_product()
Earbuds.show_product()

print()
print("......Display product list by location (group by location)......")
l_list = [Rajkot, Gandhinagar, Baroda, Ahmadabad]
Location.sort(l_list)