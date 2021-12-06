import unittest
from unittest.mock import *
from zad2.src.car import Car
from zad2.src.carimpl import CarImpl


class TestCar(unittest.TestCase):
    def test_needs_fuel_true(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carNeedsFuel(), "Car needs fuel!")

    def test_needs_fuel_false(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carNeedsFuel(), "Car doesn't need fuel.")

    def test_temperature_100(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 100
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carGetEngineTemperature(), "Car temperature is equal to 100`C")

    def test_temperature_undefined(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carGetEngineTemperature(), "Car temperature is unknown...")

    def test_driving_to_Gdansk(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = "Gdańsk"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carDriveTo("Gdańsk"), "Car is driving to Gdańsk")

    def test_not_driving(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carDriveTo(None), "Car isn't driving now.")
