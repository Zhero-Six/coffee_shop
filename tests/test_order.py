import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Price too low
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Price too high
    with pytest.raises(ValueError):
        Order("Not a customer", coffee, 5.0)  # Invalid customer
    with pytest.raises(ValueError):
        Order(customer, "Not a coffee", 5.0)  # Invalid coffee