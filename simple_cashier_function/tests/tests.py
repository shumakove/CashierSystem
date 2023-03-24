import pytest
from cashier_system import CashierSystem


def test_add_new_product_without_discount():
    cs = CashierSystem('', '')
    assert cs.add_product_to_cart('Green Tea', 3.11) == 3.11
    assert cs.add_product_to_cart('Strawberries', 5.00) == 8.11
    assert cs.add_product_to_cart('Coffee', 11.23) == 19.34


def test_add_one_new_product_with_freerule_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    cart = cs.add_product_to_cart('Green Tea', 3.11)
    assert len(cart['GR']) == 2
    assert cs.get_total_value() == 3.11


def test_add_million_products_with_freerule_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(999999):
        cart = cs.add_product_to_cart('Green Tea', 3.11)
    assert cs.get_total_value() == 3110000
    assert len(cs.get_cart()['GR']) == 1000000


def test_add_n_products_with_reducedpricerule_discunt():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(10):
        cart = cs.add_product_to_cart('Coffee', 11.23)
    assert len(cs.get_cart()['CF']) == 10
    assert len(cs.get_total_value() == 112.3)


def test_add_more_then_n_products_with_reducedpricerule_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(11):
        cs.add_product_to_cart('Coffee', 11.23)
    assert len(cs.get_cart()['CF']) == 11
    expected_total_value = 275  # hardcoded value for test positive discount value
    assert len(cs.get_total_value() == expected_total_value)


def test_add_n_products_with_fractionpricerule_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(10):
        cart = cs.add_product_to_cart('Strawberries', 5.00)
    assert len(cs.get_cart()['CF']) == 10
    assert len(cs.get_total_value() == 50)  # 50 could be replaced with parameters


def test_add_more_then_n_products_with_fractionpricerule_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(11):
        cart = cs.add_product_to_cart('Strawberries', 5.00)
    assert len(cs.get_cart()['SR']) == 10
    expected_total_value = 25  # hardcoded value for test positive discount value
    assert len(cs.get_total_value() == expected_total_value)


def test_several_products_with_discount():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(11):
        cart = cs.add_product_to_cart('Strawberries', 5.00)
    for x in range(11):
        cs.add_product_to_cart('Coffee', 11.23)
    cs.add_product_to_cart('Green Tea', 3.11)

    expected_total_value = 303.11 # hardcoded value for test positive discount value
    assert len(cs.get_total_value() == expected_total_value)

def test_product_id_index_incrimentation():
    cs = CashierSystem('products.yaml', 'rules.yaml')
    for x in range(11):
        cs.add_product_to_cart('Strawberries', 5.00)
    assert cs.get_cart()['SR'][-1]['Product Code'] == 'SR11'