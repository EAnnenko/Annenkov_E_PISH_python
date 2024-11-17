#Лабораторная №2 задача 2
a = int(input(" Введите число а: ")) 
b = int(input(" Введите число b: "))
def function(a,b): 
    while(b): 
        a, a = b, a % b 
        return a  
c = function(a, b)
print("Наибольший общий делитель") 
print(c)
