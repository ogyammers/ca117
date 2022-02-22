#!/usr/bin/env python3

class BankAccount(object):

   def set_attributes(self, name, number, balance):
      self.name = name
      self.number = number
      self.balance = balance

   def print_attributes(self):
      print(f'Name: {self.name}\nAccount number: {self.number}\nBalance: {self.balance:.2f}')

   def deposit(self, deposit):
      self.deposit = deposit
      self.balance = self.balance + self.deposit
