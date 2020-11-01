from cars import Cars
from electric_car_m import ElectricCar

my_car = ElectricCar('tesla', 'model s', 2017)
print(my_car.summary())
my_car.battery.read_battery()

your_car = Cars('toyoya', 'prius', 2000)
print(your_car.summary())
your_car.odometer_reading()
