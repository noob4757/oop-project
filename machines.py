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
        else:
            print("No fuel left.")

    def stop(self):
        self.is_driving = False
        print("Tractor stopped.")

    def refuel(self):
        self.has_fuel = True
        print("Fuel is refilled.")

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

