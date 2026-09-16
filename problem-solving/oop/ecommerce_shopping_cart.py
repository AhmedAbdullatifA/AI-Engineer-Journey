# Problem 06 — E-Commerce Shopping Cart

# Build a small E-Commerce Shopping Cart System using OOP.
# You need at least three classes:
# Product
# ShoppingCart
# Customer

# 1. Product
# Each product should contain:
# name
# price
# stock

# Example:
# product = Product("Laptop", 30000, 5)

# 2. ShoppingCart
# The cart should be able to:
# add_product(product, quantity)
# remove_product(product)
# calculate_total()
# display_cart()
# Rules

# When adding a product:
# The quantity must be positive.
# The requested quantity cannot exceed the available stock.
# If the product is already in the cart, increase its quantity rather than adding a duplicate item.

# When removing a product:
# Remove it from the cart completely.

# calculate_total() should return:
# price × quantity
# for all products.

# 3. Customer
# A customer should contain:
# name
# cart

# The customer should be able to add products to their cart and view their cart.

# Example
# laptop = Product("Laptop", 30000, 5)
# mouse = Product("Mouse", 500, 10)

# customer = Customer("Ahmed")

# customer.cart.add_product(laptop, 1)
# customer.cart.add_product(mouse, 2)

# customer.cart.display_cart()

# Possible output:

# ----- Shopping Cart -----
# Laptop x1 = 30000
# Mouse x2 = 1000
# -------------------------
# Total: 31000
# 🔥 Extra Requirements

# Your system should also support a checkout operation.

# When checkout happens:

# Calculate the total.
# Reduce the stock of each product.
# Empty the cart.
# Display the final total.

# For example:

# Checkout successful!
# Total Paid: 31000
# OOP Requirements

# This problem must demonstrate composition.

# In other words:

# Customer
#    ↓
# ShoppingCart
#    ↓
# Product

# The Customer has a ShoppingCart, and the ShoppingCart contains Product objects.

# Don't make everything one giant class.




class Product :
    def __init__(self, name, price, stock):
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.price = price
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        else:
            self.stock = stock



class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        
        elif quantity > product.stock:
            raise ValueError("Quantity exceeds available stock")
        
        else:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.stock -= quantity


    def remove_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        else:
            if product in self.items:
                if quantity > self.items[product]:
                    raise ValueError("Quantity exceeds quantity in cart")
                
                elif quantity == self.items[product]:
                    product.stock += quantity
                    del self.items[product]

                else:
                    self.items[product] -= quantity
                    product.stock += quantity


    def calculate_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    
    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for product, quantity in self.items.items():
                print(f"Name: {product.name}\nQuantity: {quantity}\nTotal: {product.price * quantity:.2f}")

    def clear_cart(self):
        self.items.clear()

    def checkout(self):
        total = self.calculate_total()
        if total > 0:
            print(f"Checkout successful!\nTotal Paid: {total:.2f}")
            self.clear_cart()
        else:
            print("Shopping cart is empty. Cannot proceed to checkout.")




class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()




Mouse = Product("Mouse", 25.99, 10)
Laptop = Product("Laptop", 999.99, 5)
Phone = Product("Phone", 499.99, 8)

c1 = Customer("Alice")

# Test 1: Add products to the cart
c1.cart.add_product(Mouse, 2)
c1.cart.add_product(Mouse, 4)   # should increase quantity, not overwrite
c1.cart.add_product(Laptop, 1)
c1.cart.add_product(Laptop, 1)  # should increase quantity
c1.cart.display_cart()
print(f"Total: {c1.cart.calculate_total():.2f}")

# Shopping Cart:
# Name: Mouse
# Quantity: 6
# Total: 155.94
# Name: Laptop
# Quantity: 2
# Total: 1999.98
# Total: 2155.92


# Test 2: Remove some products 
c1.cart.remove_product(Mouse, 3)
c1.cart.display_cart()
print(f"Total: {c1.cart.calculate_total():.2f}")

# Shopping Cart:
# Name: Mouse
# Quantity: 3
# Total: 77.97
# Name: Laptop
# Quantity: 2
# Total: 1999.98
# Total: 2077.95


# Test 3: Checkout 
c1.cart.checkout()
# Checkout successful!
# Total Paid: 2077.95

c1.cart.display_cart()
# Shopping cart is empty.

print(f"Mouse stock after checkout: {Mouse.stock}")
# Mouse stock after checkout: 7

print(f"Laptop stock after checkout: {Laptop.stock}")
# Laptop stock after checkout: 3
