class CashierSystem:

    def __init__(self, product_config, rules_config):
        self.discount_rules = None # Some logic of the loading from configurations
        self.products = None # Some logic of the loading from configurations
        self.cart = {}

    def start_session(self, new_user):
        """
        Some logic of the starting session for new user
        :param new_user: Active user
        :return:
        """
        pass

    def add_product_to_cart(self, name, price):
        """
        Function for adding new item in the cart
        :param name: Name of the product
        :param price: The value of price in funds
        :return: total_price: Total price based on all discounts
        """
        code = 'DEFAULT'
        total_value = 0

        if 'green tea' in name.lower():
            code = 'GR'

        if 'coffee' in name.lower():
            code = 'CF'

        if 'strawberries' in name.lower():
            code = 'SR'

        if code not in self.cart:
            index = code + '1'
            self.cart[code] = []
        else:
            index = code + str(len(self.cart[code]) + 1)

        self.cart[code].append({
                'Product Code': index,
                'Name': name,
                'Price': self.calculate_discount(name, price)
            }
        )

        print(f'Total price: {self.get_total_value()}')
        return self.cart

    def calculate_discount(self, product_name, original_price):
        """
        :param product_name: The name of the product for calculation the final_price
        :param original_price: The value of original price before discount
        :return: final_price: The result of discount
        """

        """
        Here some logic of depends on configurations in products.yaml and rules.yaml
        """
        # This is mock!!!
        if self.discount_rules is None:
            final_price = original_price
        else:
            pass # here is a logic of calculation
        return final_price

    def get_total_value(self):
        total_value = 0
        for category in self.cart:
            for item in self.cart[category]:
                total_value += item['Price']
        return total_value

    def get_cart(self):
        return self.cart