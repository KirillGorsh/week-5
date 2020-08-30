class Car():
    """This is class to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = 'White'
        self.odometer_reading = 0 # in miles

    #getter (return) and setter (assign a new value)
    def get_description(self):
        msg = f"Your car: \n\tManufacturer: {self.make.title()}\n\tModel: {self.model.title()}\n\tYear: {self.year}\n\tColor: {self.color}"
        return msg

    def set_color(self, new_color):
        print(f"Chaging the color {self.color} to {new_color}.")
        self.color = new_color

    def read_odometer(self):
        msg = f"Car has {self.odometer_reading} miles on it."
        return msg

    def set_odometer(self, new_miles):
        if new_miles >= self.odometer_reading:
            print(f"Setting odometer reading from {self.odometer_reading} to {new_miles}")
            self.odometer_reading = new_miles
        else:
            print(f"You can not roll back odometer from {self.odometer_reading} to {new_miles}")

    def increment_odometer(self, miles):
        """Adding :param miles to odometer_reading"""
        # self.odometer_reading = self.odometer_reading + miles
        if miles > 0:
            print(f"Incrementing odometer with more {miles} miles.")
            self.odometer_reading += miles
        else:
            print(f"Negative value can not be passed to odometer: {miles}")


class ElectricCar(Car): # Inheritting Car class
    """Represents Electric car, inherists all features of Car."""

    def __init__(self, make, model, year): # child class constructor
        super().__init__(make, model, year) # calling the constructor of parent class
        self.battery_size = 80

    def get_description(self):
        msg = f"Your car: \n\tManufacturer: {self.make}\n\tModel: {self.model}" \
              f"\n\tYear: {self.year}\n\tColor: {self.color}\n\tBattery size: {self.battery_size}"
        return msg

    def test_method(self):
        print(self.get_description()) # current class
        print(super().get_description()) # parent class
        # 'this' keyword in java is used as 'self' in python