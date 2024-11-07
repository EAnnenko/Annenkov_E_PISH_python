#Задача №3
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
sum = 0
if abs (a + b) < 100:
    for i in range(a, b + 1):
       sum += i ** 2
    print (sum)
else:
    print ("Ошибка! Недопустимое число. Число должно быть от 1 до 100.")
