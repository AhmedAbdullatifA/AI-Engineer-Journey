# Problem 08 — Payment Processing System
#
# Build a Payment Processing System using Object-Oriented Programming.
#
# The system should support different payment methods while using
# abstraction, inheritance, and polymorphism.
#
# You need at least five classes:
#
# 1. PaymentMethod
# 2. CreditCardPayment
# 3. PayPalPayment
# 4. CashPayment
# 5. PaymentProcessor
#
# --------------------------------------------------
# 1. PaymentMethod
# --------------------------------------------------
#
# PaymentMethod should be an Abstract Base Class.
#
# It should define an abstract method:
#
# pay(amount)
#
# The base class should not provide the actual payment implementation.
#
# Every payment method must implement its own version of pay().
#
# --------------------------------------------------
# 2. CreditCardPayment
# --------------------------------------------------
#
# This class should inherit from PaymentMethod.
#
# It should contain:
#
# - card_holder
# - card_number
#
# Implement the pay() method so that it processes the payment
# using a credit card.
#
# Validate the payment amount and card information when necessary.
#
# --------------------------------------------------
# 3. PayPalPayment
# --------------------------------------------------
#
# This class should inherit from PaymentMethod.
#
# It should contain:
#
# - email
#
# Implement the pay() method so that it processes the payment
# using PayPal.
#
# --------------------------------------------------
# 4. CashPayment
# --------------------------------------------------
#
# This class should inherit from PaymentMethod.
#
# It does not require any additional payment information.
#
# Implement the pay() method for cash payments.
#
# --------------------------------------------------
# 5. PaymentProcessor
# --------------------------------------------------
#
# The PaymentProcessor should be able to process any payment method.
#
# It should provide functionality similar to:
#
# process(payment_method, amount)
#
# The PaymentProcessor should NOT need to check the specific type
# of payment method.
#
# Do NOT use logic such as:
#
# if payment_type == "credit_card":
#     ...
# elif payment_type == "paypal":
#     ...
#
# Instead, rely on polymorphism.
#
# --------------------------------------------------
# Example Scenario
# --------------------------------------------------
#
# Create:
#
# - A CreditCardPayment object
# - A PayPalPayment object
# - A CashPayment object
#
# Then use the same PaymentProcessor to process payments
# using all three payment methods.
#
# --------------------------------------------------
# Requirements
# --------------------------------------------------
#
# Your program should demonstrate:
#
# - Abstract Base Classes
# - abc module
# - @abstractmethod
# - Inheritance
# - Method overriding
# - Polymorphism
# - Object interaction
# - Validation
#
# The main goal is to make different payment methods work
# through a common interface.