from zad2.src.car import Car


class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def carNeedsFuel(self):
        if self.car.needsFuel():
            return "Car needs fuel!"
        return "Car doesn't need fuel."

    def carGetEngineTemperature(self):
        if self.car.getEngineTemperature():
            temp = self.car.getEngineTemperature()
            return "Car temperature is equal to " + str(temp) + "`C"
        return "Car temperature is unknown..."

    def carDriveTo(self, destination):
        if self.car.driveTo(destination):
            return "Car is driving to " + str(destination)
        return "Car isn't driving now."
