'''
    -Create one class named "category" with members "name", "code", "no_of_products"
    -Create one class named "product" with members "name", "code", "category", "Price"
    -Create three objects of category.
    -Create 10 different products. Code must be unique.
    -Print category info with its no_of_products
    -Sort and Print products based on price (Price High to Low and Low to High) with all details.
    -Search product using its code.
'''


class Category:

    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def show(self):
        print('category name:', self.name, ',', 'code:', self.code, ',', 'no_of_products:', self.no_of_products)


class Product(Category):
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_products += 1  # logic
        self.price = price

    def show(self):
        return print('products name:', self.name, ',', 'code:', self.code, ',', 'category:', self.category.name, ',',
                     'price:', self.price)

    @staticmethod
    def short_high_to_low():
        for product in range(len(productlist)):
            for product1 in range(product + 1, len(productlist)):
                if productlist[product].price < productlist[product1].price:
                    productlist[product], productlist[product1] = productlist[product1], productlist[product]

        for product in productlist:
            product.show()

    @staticmethod
    def short_low_to_high():
        for product in range(len(productlist)):
            for product1 in range(product + 1, len(productlist)):
                if productlist[product].price > productlist[product1].price:
                    productlist[product], productlist[product1] = productlist[product1], productlist[product]

        for product in productlist:
            product.show()

    @staticmethod
    def search_product_using_code():
        x = int(input("Enter the code"))
        for product in productlist:
            if product.code == x:
                product.show()


# Three object of category
c1 = Category("laptop", 201)
c2 = Category("mobile", 201)
c3 = Category("tv", 301)

# Ten products
p1 = Product("hp", 101, c1, 4500)
p2 = Product("asus", 102, c1, 3500)
p3 = Product("dell", 103, c1, 2500)
p4 = Product("redmi", 201, c2, 2500)
p5 = Product("vivo", 202, c2, 1500)
p6 = Product("one plus", 203, c2, 2000)
p7 = Product("oppo", 204, c2, 1200)
p8 = Product("sony", 301, c3, 5500)
p9 = Product("samsung", 302, c3, 4500)
p10 = Product("lg", 303, c3, 3500)

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

print("-----Number of product with show-----")
c1.show()
c2.show()
c3.show()

productlist = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# sort and print products based on price (high_to_low & low_to_high) with all details.
print("-----price print high to low and low to high-----")

print(">>>>>high to low price<<<<<")
print(Product.short_high_to_low())

print(">>>>>low to high price<<<<<")
print(Product.short_low_to_high())

# search product using code
print("-----search product using code-----")
Product.search_product_using_code()
