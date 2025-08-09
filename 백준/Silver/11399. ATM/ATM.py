import sys
sys.setrecursionlimit(10**5)

N = int(input())
array = list(map(int, input().split()))
sum = 0

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

narray = quick_sort(array)

for i in range(N):
    sum += narray[i] * (N - i)
print(sum)
