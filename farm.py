class Field:
    SEED_PRICES = {
        'banana': 10,
        'pineapple': 100,
        'watermelon': 1000
    }

    HARVEST_PROFITS = {
        'banana': 50,
        'pineapple': 500,
        'watermelon': 5000
    }

    GROWTH_DAYS = {
        'banana': 3,
        'pineaplle': 4,
        'watermelon': 5
    }

    FIELD_STATES = ['unplowed', 'plowed', 'planted', 'ready for harvest']

    def __init__(self):
        self.state = self.FIELD_STATES[0]  # Initial state is 'unplowed'
        self.balance = 10  # Starting balance
        self.seeds = {seed: 0 for seed in Field.SEED_PRICES.keys()}  # Initial seed inventory
        self.current_seed = None
        self.days_until_harvest = 0

    def plow(self):
        if self.state == self.FIELD_STATES[0]:  # unplowed
            self.state = self.FIELD_STATES[1]  # plowed
            print("The field has been plowed.")
        else:
            print("The field is already plowed or in a state that cannot be plowed again.")

    def plant(self, seed_type=None):
        if self.state == self.FIELD_STATES[1]:  # plowed
            if seed_type and self.seeds.get(seed_type, 0) > 0:
                self.seeds[seed_type] -= 1
                self.state = self.FIELD_STATES[2]  # planted
                self.current_seed = seed_type
                self.days_until_harvest = Field.GROWTH_DAYS[seed_type]
                print(f"Seeds of {seed_type} have been planted in the field.")
            else:
                print(f"Cannot plant {seed_type}. Insufficient seeds or invalid type.")
        else:
            print("The field needs to be plowed before planting.")

    def harvest(self):
        if self.state == self.FIELD_STATES[3]:  # ready for harvest
            profit = Field.HARVEST_PROFITS[self.current_seed]
            self.balance += profit
            print(f"The field has been harvested. Profit: {profit}. Current balance: {self.balance}.")
            self.state = self.FIELD_STATES[0]  # Reset the field state to 'unplowed' after harvesting
            self.current_seed = None  # Clear the seed type after harvesting
        else:
            print("The field is not ready for harvesting.")

    def buy_seeds(self, seed_type, quantity):
        if seed_type in Field.SEED_PRICES:
            total_cost = Field.SEED_PRICES[seed_type] * quantity
            if self.balance >= total_cost:
                self.balance -= total_cost
                self.seeds[seed_type] += quantity
                print(f"Bought {quantity} {seed_type} seeds for {total_cost}. Current balance: {self.balance}.")
            else:
                print("Insufficient balance to buy seeds.")
        else:
            print("Invalid seed type.")

    def pass_day(self):
        if self.state == self.FIELD_STATES[2] and self.days_until_harvest > 0:  # planted
            self.days_until_harvest -= 1
            if self.days_until_harvest == 0:
                self.state = self.FIELD_STATES[3]  # ready for harvest
                print(f"The {self.current_seed} is ready for harvest.")
            else:
                print(f"{self.days_until_harvest} days left until the {self.current_seed} is ready for harvest.")
        else:
            print("No crops growing or already ready for harvest.")