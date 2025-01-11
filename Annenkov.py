
from operator import mul
a = input('введите число')
if int(a)<0:
    print('Введено отрицательное число!')
else:
    summa = 0
    mult = 1
    for digit in a:
            summa += int(digit)
            mult *= int(digit)
    if summa==mult:
        print("***Сумма равна произведению***")
    else:
        print("***Сумма не равна произведению***")
        
