
import copy

# Вариант 1 на основе лаб 3_1
a = input('Введите последовательность чисел через пробел для первой строки матрицы: ')
arr1 = [int(i) for i in a.split(' ') if i.isdigit()]
b = input('Введите последовательность чисел через пробел для второй строки матрицы: ')
arr2 = [int(i) for i in b.split(' ') if i.isdigit()]
c = input('Введите последовательность чисел через пробел для третьей строки матрицы: ')
arr3 = [int(i) for i in c.split(' ') if i.isdigit()]
d = 2
def reverseArray(arr1,d):
    c=(arr1[d:])+(arr1[:d])
    return c
def reverseArray(arr2,d):
    c=(arr2[d:])+(arr2[:d])
    return c
def reverseArray(arr3,d):
    c=(arr3[d:])+(arr3[:d])
    return c
print(reverseArray(arr1,d), reverseArray(arr2,d), reverseArray(arr3,d))

#Вариант 2 на основе выборки и копирования
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
copy_matrix = copy.deepcopy(matrix)
arr1 = copy_matrix[0]
arr2 = copy_matrix[1]
arr3 = copy_matrix[2]
d = 1
def reverseArray(arr1,d):
    c=(arr1[d:])+(arr1[:d])
    return c
def reverseArray(arr2,d):
    d=(arr2[d:])+(arr2[:d])
    return d
def reverseArray(arr3,d):
    e=(arr3[d:])+(arr3[:d])
    return e
print(reverseArray(arr1,d), reverseArray(arr2,d), reverseArray(arr3,d))