import tkinter as tk
from tkinter import ttk
from machines import *
from farm import *

class FarmingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Farming Simulator")
        self.root.geometry("600x500")

        self.tractor = Tractor("BMW", "X500", has_fuel=True)
        self.field = Field()

        self.attach_plow_button = ttk.Button(root, text="Attach Plow", command=self.attach_plow)
        self.attach_planter_button = ttk.Button(root, text="Attach Planter", command=self.attach_planter)
        self.attach_harvester_button = ttk.Button(root, text="Attach Harvester", command=self.attach_harvester)
        self.detach_implement_button = ttk.Button(root, text="Detach Implement", command=self.detach_implement)
        self.drive_button = ttk.Button(root, text="Drive Tractor", command=self.drive_tractor)
        self.stop_button = ttk.Button(root, text="Stop Tractor", command=self.stop_tractor)
        self.refuel_button = ttk.Button(root, text="Refuel Tractor", command=self.refuel_tractor)
        self.pass_day_button = ttk.Button(root, text="Wait a Day", command=self.pass_day)
        self.buy_banana_button = ttk.Button(root, text="Buy Banana Seeds", command=self.buy_banana_seeds)
        self.buy_pineapple_button = ttk.Button(root, text="Buy Pineapple Seeds", command=self.buy_pineapple_seeds)
        self.buy_watermelon_button = ttk.Button(root, text="Buy Watermelon Seeds", command=self.buy_watermelon_seeds)
        self.balance_label = ttk.Label(root, text="Balance: $")
        self.seed_label = ttk.Label(root, text="Seeds: ")

        self.attach_plow_button.grid(row=0, column=0, padx=5, pady=5)
        self.attach_planter_button.grid(row=0, column=1, padx=5, pady=5)
        self.attach_harvester_button.grid(row=0, column=2, padx=5, pady=5)
        self.detach_implement_button.grid(row=0, column=3, padx=5, pady=5)
        self.drive_button.grid(row=1, column=0, padx=5, pady=5)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)
        self.refuel_button.grid(row=1, column=2, padx=5, pady=5)
        self.pass_day_button.grid(row=1, column=3, padx=5, pady=5)
        self.buy_banana_button.grid(row=2, column=0, padx=5, pady=5)
        self.buy_pineapple_button.grid(row=2, column=1, padx=5, pady=5)
        self.buy_watermelon_button.grid(row=2, column=2, padx=5, pady=5)
        self.balance_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.seed_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.update_balance()
        self.update_seeds()

    def attach_plow(self):
        self.tractor.attach_implement(Plow())

    def attach_planter(self):
        self.tractor.attach_implement(Planter())

    def attach_harvester(self):
        self.tractor.attach_implement(Harvester())

    def detach_implement(self):
        self.tractor.detach_implement()

    def drive_tractor(self):
        self.tractor.drive(self.field)

    def stop_tractor(self):
        self.tractor.stop()

    def refuel_tractor(self):
        self.tractor.refuel()

    def pass_day(self):
        self.field.pass_day()
    def buy_banana_seeds(self):
        self.field.buy_seeds("banana", 1)
        self.update_balance()
        self.update_seeds()

    def buy_pineapple_seeds(self):
        self.field.buy_seeds("pineapple", 1)
        self.update_balance()
        self.update_seeds()

    def buy_watermelon_seeds(self):
        self.field.buy_seeds("watermelon", 1)
        self.update_balance()
        self.update_seeds()

    def update_balance(self):
        self.balance_label.config(text="Balance: $" + str(self.field.balance))

    def update_seeds(self):
        seeds_text = "Seeds: "
        for seed, quantity in self.field.seeds.items():
            seeds_text += f"{seed}: {quantity} "
        self.seed_label.config(text=seeds_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = FarmingApp(root)
    root.mainloop()