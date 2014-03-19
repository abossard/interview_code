import random
import timeit
udata = [x for x in range(0,10000)]
random.shuffle(udata)
udata2 = [x for x in range(0,10000)]
random.shuffle(udata2)
#udata = [0,2,1,3]


def insertion_sort(data):
    n = len(data)
    for pos in range(1, n):
        value = data[pos]
        # print "took data[%s]: %s" % (pos,value)
        # print "comparing with data[%s]: %s" % (pos - 1,data[pos - 1])
        while pos > 0 and data[pos - 1] > value:
            data[pos] = data[pos - 1]
            pos = pos - 1
        data[pos] = value

print timeit.timeit("insertion_sort(udata)", setup="from __main__ import insertion_sort, udata", number=100)
print udata

def merge(left, right):
    result = list()
    left_pos = 0
    right_pos = 0
    while left_pos < len(left) or right_pos < len(right):
        if left_pos < len(left) and (right_pos == len(right) or left[left_pos] < right[right_pos]):
            result.append(left[left_pos])
            left_pos += 1
        else:
            result.append(right[right_pos])
            right_pos += 1
    return result

def mergesort(data):
    n = len(data)
    if n <= 1:
        return data
    middle = int(n / 2)
    left_half = mergesort(data[0:middle])
    right_half = mergesort(data[middle:])
    return merge(left_half, right_half)

print mergesort(udata2)
print timeit.timeit("mergesort(udata2)", setup="from __main__ import mergesort, merge, udata2", number=100)

def msort4(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x)/2)
    y = msort4(x[:mid])
    z = msort4(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result

random.shuffle(udata2)
print timeit.timeit("msort4(udata2)", setup="import random;from __main__ import udata2, msort4;random.shuffle(udata2)", number=100)

print timeit.timeit("sorted(x)", setup="import random;x=range(10000);random.shuffle(x)", number=100)

print timeit.timeit("x.sort()", setup="import random;x=range(10000);random.shuffle(x)", number=100)
