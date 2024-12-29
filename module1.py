#Лабораторная №2 задача 1
x = int(input("""
              Лабораторная №2 задача 1
              Введите х: """))
if -2 <= x < 2:
    a = x ** 2
    print (a)
else:
    if x >=2:
        b = x ** 2 + 4 * x + 5
        print (b)
    else:
        if x < -2:
            print (4)
