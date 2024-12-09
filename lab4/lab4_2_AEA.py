# Лаб. раб 4. Задача 2
string = "abracadabra"
set_string = set(string)
dct = dict()
for word in set_string :
    dct[word] = string.count(word)
print(dct)