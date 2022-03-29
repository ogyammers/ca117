from triathlon_v3_111 import Triathlete, Triathlon

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('ZAlan Wren', 23)
    t4 = Triathlete('Jane Brown', 24)
    t5 = Triathlete('Johnny Squire', 25)
    t6 = Triathlete('Ian Wren', 26)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    t4.add_time('swim', 100)
    t4.add_time('cycle', 120)
    t4.add_time('run', 150)

    t5.add_time('swim', 400)
    t5.add_time('cycle', 120)
    t5.add_time('run', 250)

    t6.add_time('swim', 40)
    t6.add_time('cycle', 20)
    t6.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)
    tn.add(t4)
    tn.add(t5)
    tn.add(t6)


    print(tn.best())
    print(tn.worst())
    print(tn)

if __name__ == '__main__':
    main()