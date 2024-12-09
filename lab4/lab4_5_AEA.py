# Лаб. раб 4. Задача 5
string1 = "abracadabra"
string2 = "abracadabra"
set_string = set(string1)
dict1 = dict()
for word in set_string :
    dict1[word] = string1.count(word)
dict2 = dict()
for word in set_string :
    dict2[word] = string2.count(word)
if dict1 == dict2:
      print ("Обе строки — анаграммы")
else:
     print ("Обе строки — не анаграммы")