'''
● Add new data members “parent”, “display_name”, “products” (list of product objects)
inside category class.
● Add a new member function to generate “display_name”.
● “display_name” has text value as below.
     Vehicle category without parent then “Vehicle”
     Car category with “Vehicle” as parent then “Vehicle > Car”
     Petrol category with “Car” as parent then “Vehicle > Car > Petrol”
● Create 5 category objects with parent and child relation.
● Create 3 product objects in each category.
● Display Category with its Code, Display Name and all product details inside that
category.
● Display product list by category ( group by category, order by category name).
'''



class Category:
    def __init__(self, name, code, parent=None):

        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self.parent_display_name()
        self.no_of_product = 0
        self.product = []

    def parent_display_name(self):
        if self.parent is None:
            return self.name
        else:
            return str(self.parent.parent_display_name()) + " " + ">" + " " + str(self.name)         # logic (recursion)

    def order_category(self):
        for category in range(len(category_list)):
            for category1 in range(category + 1, len(category_list)):
                if category_list[category].name > category_list[category1].name:
                    category_list[category], category_list[category1] = category_list[category1], category_list[category]
        for category in category_list:
            print("category name:", category.name)
            for product in category.product:
                print("product show:", product)
            print()

    def show(self):
        print("category name:", self.name, '\n', "code:", self.code, '\n', "no_of_product:", self.no_of_product, '\n', "display name:", self.display_name)
        for product in self.product:
            print("product:", product)
        print()

class Product(Category):

    def __init__(self, name, code, category, price):
            self.name = name
            self.code = code
            self.category = category
            category.no_of_product += 1             # logic
            category.product.append(self)           # logic
            self.price = price

    def __repr__(self):                              # object(attribute show thay)
         return self.category.name + " " + ":" + " " + self.name + " " + "," + " " +str(self.code) + " " + "," + " " + self.category.name + " " + "," + " " + str(self.price)

    def show(self):
        return print("product name:", self.name, "|", "code:", self.code, "|", "category:", self.category.name, "|", "price:", self.price)


# create 5 category object with parent and child relation
c1 = Category("TV", 101)
c2 = Category("Laptop", 201, c1)
c3 = Category("Mobile", 301, c2)
c4 = Category("Smart watch", 401, c3)
c5 = Category("earbuds", 501, c4)

category_list = [c1, c2, c3, c4, c5]

# create 3 product objects in each category
p1 = Product("Sony", 601, c1, 36000)
p2 = Product("Lg", 602, c1, 28000)
p3 = Product("Samsung", 603, c1, 25000)
p4 = Product("Hp", 701, c2, 40000)
p5 = Product("Asus", 702, c2, 37000)
p6 = Product("Dell", 703, c2, 35000)
p7 = Product("Redmi", 704, c3, 20000)
p8 = Product("Vivo", 705, c3, 18000)
p9 = Product("Oppo", 706, c3, 15000)
p10 = Product("Fossil", 707, c4, 10000)
p11 = Product("Apple", 708, c4, 8000)
p12 = Product("Fitbit", 709, c4, 7000)
p13 = Product("Noise", 801, c5, 5000)
p14 = Product("Croma", 802, c5, 3000)
p15 = Product("Boat", 803, c5, 2000)

p1.show()
p2.show()
p3.show()
p4.show()
p5.show()
p6.show()
p7.show()
p8.show()
p9.show()
p10.show()
p11.show()
p12.show()
p13.show()
p14.show()
p15.show()

print()
print("-----List of product objects-----")
print("-----Display category with its code, Display name and all product details-----")

c1.show()
c2.show()
c2.show()

print()
print("-----Display product list by category-----")
Category.order_category(category_list)
