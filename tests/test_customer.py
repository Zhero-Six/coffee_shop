import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long
    with pytest.raises(ValueError):
        Customer(123)  # Not a string

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order in customer.orders()
    assert coffee in customer.coffees()

def test_most_aficionado():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer1.create_order(coffee, 3.0)
    customer2.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) == customer1