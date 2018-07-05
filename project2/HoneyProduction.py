class HoneyProduction:
    def __init__(self, state, number_of_colonies, yield_per_colony, total_production, stocks, price_per_lb, production_value, year):
        self.state = state
        self.number_of_colonies = number_of_colonies
        self.yield_per_colony = yield_per_colony
        self.total_production = total_production
        self.stocks = stocks
        self.price_per_lb = price_per_lb
        self.production_value = production_value
        self.year = year

    def __str__(self):
        print("State: " + self.state + " ,total production: " + str(self.total_production) + " ,production value: " + str(self.production_value) + " ,year: " + str(self.year))

    def get_total_production(self, year):
        if self.year == year:
            return self.total_production
        else:
            return False

    def get_production_value(self, year):
        if self.year == year:
            return self.production_value
        else:
            return False

    def get_state(self, year):
        if self.year == year:
            return self.state
        else:
            return False
