#!/usr/bin/env python3

import sys
import calendar

poem = ["Monday's child is fair of face.",
        "Tuesday's child is full of grace.",
        "Wednesday's child is full of woe.",
        "Thursday's child has far to go.",
        "Friday's child is loving and giving.",
        "Saturday's child works hard for a living.",
        "Sunday's child is fair and wise and good in every way."]


for line in sys.stdin:
   [day, month, year] = line.strip().split()
   n = calendar.weekday(int(year), int(month), int(day))
   day = (poem[n].split()[0].split("'")[0])
   print("You were born on a" + " " + day + " and " + poem[n])
