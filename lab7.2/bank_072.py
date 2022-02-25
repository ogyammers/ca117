#!/usr/bin/env python3

class BankAccount(object):

   def __init__(self, balance=0):
      self.balance = balance

   def __str__(self):
      return f'Your current balance is {self.balance:.2f} euro'

   def deposit(self, deposit):
      self.balance = self.balance + deposit

   def withdraw(self, withdraw):
      if self.balance >= withdraw:
         self.balance = self.balance - withdraw
