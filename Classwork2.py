## б. Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

for i in range(2,10):
    for j in range(2,6):
        print(j, "*", i, "=", j*i, end="\t")
    print("")
    
print("")

for i in range(2,10):
    for j in range(6,10):
        print(j, "*", i, "=", j*i, end="\t")
    print("")