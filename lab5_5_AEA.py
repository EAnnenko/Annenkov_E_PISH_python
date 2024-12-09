# Лаб. раб 5. Задача 5
text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."
list = text.split()
list1 = []
for word in list:
    if word.isnumeric():
        list1.append(int(word))
print(list1)