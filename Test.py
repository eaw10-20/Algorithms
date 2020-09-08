from Sort import Sort
import random

ary = [random.randrange(50)+1 for i in range(25)]
print(ary)
sorter = Sort()
new = sorter.mergeSort(ary)
print(new)