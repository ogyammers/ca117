def service(mileage):
   return 10000 - (mileage % 10000)


class Vehicle(object):
   def __init__(self, vin, cat, mileage, drivers=None):
      self.vin = vin
      self.cat = cat
      self.mileage = mileage
      if drivers is None:
         self.drivers = []
      else:
         self.drivers = drivers

   def add_driver(self, driver):
      self.drivers.append(driver)

   def __str__(self):
      return f'ID: {self.vin}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {", ".join(self.drivers)}\nService due in {service(self.mileage)} miles'
