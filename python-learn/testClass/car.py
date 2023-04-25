class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """ 电车 """

    def __init__(self,make,model,year,battery_size=70):
        super().__init__(make,model,year)
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has " + str(self.battery_size) + "-KM battery")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_car = Car("BMW","330Li","2020")
print(my_car.get_descriptive_name())

my_electric_car_byd = ElectricCar("BYD","Qing","2020")
print(my_electric_car_byd.get_descriptive_name())
my_electric_car_byd.describe_battery()

my_electric_car_tesla = ElectricCar("Tesla","modelS","2020",800)
print(my_electric_car_tesla.get_descriptive_name())
my_electric_car_tesla.describe_battery()