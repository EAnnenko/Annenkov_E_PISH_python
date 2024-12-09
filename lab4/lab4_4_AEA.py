# Лаб. раб 4. Задача 4
x = int(input("Введите целое число: "))
def dict(x):
    d= {}
    for i in range(1,x+1):
        d[i] = i ** 2
    return d
print(dict(x))