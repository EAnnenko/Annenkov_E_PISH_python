data = "Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия"
result_str = data.replace(";", ",")
a = result_str.split(",")
b = a[0:3]
c = a[3:6]
d = a[6:]
x = int(input("Введите ID: "))
if x == 1:
    print ("Имя:", b[0])
    print ("Возраст:", b[1])
    print ("Факультет:", b[2])
if x == 2:
        print ("Имя:", c[0])
        print ("Возраст:", c[1])
        print ("Факультет:", c[2])
if x == 3:
            print ("Имя:", d[0])
            print ("Возраст:", d[1])
            print ("Факультет:", d[2]) 
if x > 3:
                print ("Введен неверный ID")
#print (d)
#print ("Имя:", a[0])
#print ("Возраст:", a[1])
#print ("Факультет:", a[2])
