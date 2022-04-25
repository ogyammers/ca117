from fleet_v2_132 import Fleet, Vehicle

def main():
    v1 = Vehicle(21, 'van', 9100, ['joe'])
    v2 = Vehicle(22, 'car', 33000, ['mary'])
    v3 = Vehicle(33, 'truck', 16000, ['max', 'joe'])
    v4 = Vehicle(38, 'van', 18212, ['martha', 'joe'])

    f = Fleet()

    f.add(v1)
    f.add(v2)
    f.add(v3)
    f.add(v4)

    print(f.get_drivers_by_category('van'))

if __name__ == '__main__':
    main()
