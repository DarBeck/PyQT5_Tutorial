class Vehicle:

    vehicles = []

    def __init__(self, reg_num, manufacturer, year):
        self.__reg_num = reg_num
        self.__manufacturer = manufacturer
        self.__year = year
        self.add_vehicle(self.__reg_num)
        #Vehicle.vehicles.append(self.__reg_num)

    def __str__(self):
        vehicle_info = "Registration Num: %s \nManufacturer: %s \n" \
                       "Year: %s" % (self.__reg_num, self.__manufacturer, self.__year)
        return vehicle_info

    def get_reg_num(self):
        return self.__reg_num

    def set_reg_num(self, reg_num):
        self.__reg_num = reg_num

    @classmethod
    def add_vehicle(cls, vehicle):
        if vehicle not in Vehicle.vehicles and cls.__name__ is not "Vehicle":
            Vehicle.vehicles.append(vehicle)
            cls.vehicles.append(vehicle)
        else:
            print("Error: Vehicle could not be added.")

class Sedan(Vehicle):

    vehicles = []

    def __init__(self, reg_num, manufacturer, year):
        super().__init__(reg_num, manufacturer, year)
        self.__doors = 4
        self.__seating = 5
        self.__class = "Sedan"
        Sedan.vehicles.append(self.get_reg_num())

    def __str__(self):
        vehicle_info = "%s \nDoors: %s \nSeating: %s \nClass: %s" % (
            super().__str__(), self.__doors, self.__seating, self.__class
        )
        return vehicle_info

class Coupe(Vehicle):

    vehicles = []

    def __init__(self, reg_num, manufacturer, year):
        super().__init__(reg_num, manufacturer, year)
        self.__doors = 2
        self.__seating = 2
        self.__class = "Coupe"
        Coupe.vehicles.append(self.get_reg_num())

    def __str__(self):
        vehicle_info = "%s \nDoors: %s \nSeating: %s \nClass: %s" % (
            super().__str__(), self.__doors, self.__seating, self.__class
        )
        return vehicle_info


#v1 = Vehicle("A74758", "Toyota", "2016")
v2 = Sedan("B28384", "Honda", "2017")
v3 = Coupe("C39389", "BMW", "2015")
#v3 = Coupe("C39389", "BMW", "2015")
print(v2)
print(Vehicle.vehicles)
