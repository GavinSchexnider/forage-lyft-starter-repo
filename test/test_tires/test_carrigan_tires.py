import unittest

from tire import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 
        last_service_mileage = 0
        tire = CarriganTires(current_mileage, last_service_mileage)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        current_mileage = 
        last_service_mileage = 0
        tire = CarriganTire(current_mileage, last_service_mileage)
        self.assertFalse(tire.needs_service())