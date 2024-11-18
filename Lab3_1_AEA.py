a = input('Введите последовательность чисел через пробел: ')
arr = [int(i) for i in a.split(' ') if i.isdigit()]
d = 2
def reverseArray(arr,d):
    c=(arr[d:])+(arr[:d])
    return c
print(reverseArray(arr,d))