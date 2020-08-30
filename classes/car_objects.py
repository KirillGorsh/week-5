from classes.cars import Car
from classes.cars import ElectricCar


car1 = Car('toyota', 'highlander', '2020')
print(car1.get_description())
car1.set_color('red')
print(car1.get_description())

print(car1.read_odometer())
print(car1.odometer_reading)

car1.odometer_reading = 1000
print(car1.read_odometer())
print(car1.odometer_reading)

car1.set_odometer(800)
print(car1.read_odometer())
print(car1.odometer_reading)

car1.set_odometer(1500)
print(car1.read_odometer())

car1.increment_odometer(-500)
print(car1.read_odometer())

car1.increment_odometer(400)
print(car1.read_odometer())

ecar1 = ElectricCar('Tesla', 'Model Y', '2020')
print(ecar1.get_description())
ecar1.set_color('Blue')
print(ecar1.get_description())
print('-------------------')
ecar1.test_method()