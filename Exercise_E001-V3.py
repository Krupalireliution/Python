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

class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

