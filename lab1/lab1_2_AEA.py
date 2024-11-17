#Задача №2
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
if abs(a + b) < 100:
    for i in range(a, b + 1):
        print (format(i ** 2))
else:
    print ("Ошибка! Недопустимое число. Число должно быть от 1 до 100.")
