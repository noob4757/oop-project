class Tractor:
    def __init__(self, make, model, has_fuel):
        self.make = make
        self.model = model
        self.has_fuel = has_fuel
        self.is_driving = False
        self.implement_attached = None

    def drive(self, field):
        if self.has_fuel:
            self.is_driving = True
            self.has_fuel = False
            print("Tractor is driving.")
            if self.implement_attached:
                self.implement_attached.operate(field)
                self.implement_attached = None
                print("Out of fuel, please refuel and re-attach implement.")
        else:
            print("No fuel left.")
    # detach implement automatically after using fuel

    def stop(self):
        self.is_driving = False
        print("Tractor stopped.")

    def refuel(self):
        if self.is_driving == False:
            self.has_fuel = True
            print("Fuel is refilled.")
        else:
            print("Stop the tractor first.")

    def attach_implement(self, implement):
        if not self.implement_attached:
            self.implement_attached = implement
            implement.attached = True
            print(f"{implement} attached to the tractor.")
        else:
            print("An implement is already attached.")

    def detach_implement(self):
        if self.implement_attached:
            print(f"{self.implement_attached}  detached from the tractor.")
            self.implement_attached = None
        else:
            print("No implement is attached.")
    # changed so it doesn't take attribute anymore

class Implement:
    def __init__(self, attached=False):
        self.attached = attached

    def operate(self, field):
        raise NotImplementedError("This method should be implemented by subclasses.")


class Plow(Implement):
    def __init__(self, attached=False):
        super().__init__(attached)

    def operate(self, field):
        if self.attached:
            field.plow()
        else:
            print("Plow is not attached to the tractor.")


class Planter(Implement):
    def __init__(self, attached=False):
        super().__init__(attached)

    def operate(self, field):
        if self.attached:
            seed_type = input("Enter seed type to plant (banana, pineapple, watermelon): ")
            field.plant(seed_type)
        else:
            print("Planter is not attached to the tractor.")


class Harvester(Implement):
    def __init__(self, attached=False):
        super().__init__(attached)

    def operate(self, field):
        if self.attached:
            field.harvest()
        else:
            print("Harvester is not attached to the tractor.")

class Water_tank(Implement):
    def __init__(self, attached=False, has_water=False):
        super().__init__(attached)
        self.has_water = has_water
    def operate(self, field):
        if self.attached:
            if self.has_water:
                field.water()
            else:
                print("Fill the water first.")
    def refill_water(self):
        if not self.has_water:
            self.has_water = True
            print("Water has been filled.")
        else:
            print("Water tank is full.")


