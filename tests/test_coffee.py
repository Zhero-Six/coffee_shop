import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_initialization():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(ValueError):
        Coffee("Mo")  # Too short
    with pytest.raises(ValueError):
        Coffee(123)  # Not a string

def test_coffee_orders_and_customers():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = customer.create_order(coffee, 4.0)
    assert order in coffee.orders()
    assert customer in coffee.customers()

def test_num_orders_and_average_price():
    coffee = Coffee("Cappuccino")
    customer = Customer("Bob")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 3.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0