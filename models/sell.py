class Sell:
    def __init__(self, price, house, buyer, date_time):
        self.price = price
        self.house = house
        self.buyer = buyer
        self.date_time = date_time

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_house(self):
        return self.house

    def set_house(self, house):
        self.house = house

    def get_buyer(self):
        return self.buyer

    def set_buyer(self, buyer):
        self.buyer = buyer

    def get_date_time(self):
        return self.date_time

    def set_date_time(self, date_time):
        self.date_time = date_time
