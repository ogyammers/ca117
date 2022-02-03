def swap_unique_keys_values(d):
   values = [value for value in d.values()]
   unique = [value for value in values if values.count(value) == 1]
   return {d[key]: key for key in d if d[key] in unique}
