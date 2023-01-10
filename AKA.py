import random
import timeit
import matplotlib.pyplot as plt
import pandas as pd

def shellSort(array, n):
    n = len(array)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j= i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


def bubbleSort(array, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

N = 10
arr = list(range(1,N + 1))
random.shuffle(arr)
start = timeit.default_timer()
bubbleSort(arr,N)
stop = timeit.default_timer()
execution_time = stop - start
start1 = timeit.default_timer()
shellSort(arr, N)
stop1 = timeit.default_timer()
execution_time1 = stop1 - start1

N = 100
arr = list(range(1,N + 1))
random.shuffle(arr)
start = timeit.default_timer()
bubbleSort(arr,N)
stop = timeit.default_timer()
execution_time2 = stop - start
start1 = timeit.default_timer()
shellSort(arr, N)
stop1 = timeit.default_timer()
execution_time3 = stop1 - start1

N = 1000
arr = list(range(1,N + 1))
random.shuffle(arr)
start = timeit.default_timer()
bubbleSort(arr,N)
stop = timeit.default_timer()
execution_time4 = stop - start
start1 = timeit.default_timer()
shellSort(arr, N)
stop1 = timeit.default_timer()
execution_time5 = stop1 - start1

N = 10000
arr = list(range(1,N + 1))
random.shuffle(arr)
start = timeit.default_timer()
bubbleSort(arr,N)
stop = timeit.default_timer()
execution_time6 = stop - start
start1 = timeit.default_timer()
shellSort(arr, N)
stop1 = timeit.default_timer()
execution_time7 = stop1 - start1

xb = [10, 100, 1000, 10000]
yb = [execution_time,execution_time2,execution_time4,execution_time6]

xs = [10, 100, 1000, 10000]
ys = [execution_time1,execution_time3,execution_time5,execution_time7]

df = pd.DataFrame(list(zip(yb, ys)), index = ['10', '100', '1000', '10000'], columns =['Bubble Sort', 'Shell Sort'])
print(df)

plt.plot(xb, yb, label = "Bubble Sort")
plt.plot(xs, ys, label = "Shell Sort")
plt.xlabel('n')
plt.ylabel('waktu(detik)')
plt.title('Perbandingan runtime sortting')
plt.legend()
plt.show