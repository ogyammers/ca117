#!/usr/bin/env python3

import sys

def price(prices):
   if len(prices) < 3:
      return sum(prices)
   i = 1
   while i < len(prices) - 1:
      if prices[i] < prices[1 + 1] and prices[i] < prices[i - 1]:
         prices.remove(prices[i])
      elif prices[i + 1] < prices[i] and prices[i + 1] < prices[i - 1]:
         prices.remove(prices[i + 1])
      elif prices[i - 1] < prices[1 + 1] and prices[i - 1] < prices[i]:
         prices.remove(prices[i - 1])
      else:
         prices.remove(prices[i])
      i = i + 2
   return sum(prices)

def main():
   lines = [line.strip().split() for line in sys.stdin]
   for prices in lines:
      prices = [int(price) for price in prices]
      print(price(sorted(prices, reverse=True)))


if __name__ == '__main__':
   main()
