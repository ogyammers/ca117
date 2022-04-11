class Vehicle(object):
   def __init__(self, vin, cat, mileage, drivers):
      self.vin = vin
      self.cat = cat
      self.mileage = mileage
      self.drivers = drivers

   def __str__(self):
      return f'ID: {self.vin}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {", ".join(self.drivers)}'
