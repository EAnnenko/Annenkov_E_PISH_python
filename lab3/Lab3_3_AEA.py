#Задача №4
import sys
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
K = 3
N = len(arr)
def maximumSum(A, N, K):
    curr_sum = 0
    max_sum = -sys.maxsize - 1
    for i in range(N - K + 1):
        dupl_arr = A[i:i + K]
        dupl_arr.sort()
        flag = True
        for j in range(1, K, 1):
            if (dupl_arr[j] - dupl_arr[j - 1] != 1):
                flag = False
                break
        if (flag):
            temp = 0
            curr_sum = temp
            curr_sum = sum(dupl_arr)
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
    return max_sum
print(maximumSum(arr, N, K))
