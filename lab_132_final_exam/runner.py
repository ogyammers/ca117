from fleet_v2_132 import Fleet, Vehicle

def main():
    v1 = Vehicle(21, 'van', 9100, ['joe', 'max', 'dolly'])
    v2 = Vehicle(22, 'car', 33000, ['mary'])
    v3 = Vehicle(33, 'truck', 16000, ['max', 'joe'])
    v4 = Vehicle(38, 'van', 18212, ['joe', 'max', 'larry', 'dolly'])
    v5 = Vehicle(40, 'van', 18312, ['joe', 'max', 'larry', 'dolly'])

    f = Fleet()

    f.add(v1)
    print(f.get_drivers_by_category('van'))
    f.add(v2)
    print(f.get_drivers_by_category('van'))
    f.add(v3)
    print(f.get_drivers_by_category('van'))
    f.add(v4)
    print(f.get_drivers_by_category('van'))
    f.add(v5)
    print(f.get_drivers_by_category('van'))

if __name__ == '__main__':
   main()