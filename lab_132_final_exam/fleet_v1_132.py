class Vehicle(object):
   def __init__(self, vin, cat, mileage, drivers):
      self.vin = vin
      self.cat = cat
      self.mileage = mileage
      self.drivers = drivers

   def __str__(self):
      return f'ID: {self.vin}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {", ".join(self.drivers)}'

class Fleet(object):
   def __init__(self):
      self.d = {}

   def add(self, v):
      self.d[v.vin] = v

   def remove(self, vin):
      if vin in self.d:
         del self.d[vin]

   def lookup(self, vin):
      if vin in self.d:
         return self.d[vin]
      return None
