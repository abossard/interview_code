import random
udata = [x for x in range(0,1000)]
random.shuffle(udata)
#udata = [0,2,1,3]


def insertion_sort(data):
    n = len(data)
    for pos in range(1, n):
        value = data[pos]
        print "took data[%s]: %s" % (pos,value)
        print "comparing with data[%s]: %s" % (pos - 1,data[pos - 1])
        while pos > 0 and data[pos - 1] > value:
            data[pos] = data[pos - 1]
            pos = pos - 1
        data[pos] = value

insertion_sort(udata)
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

print mergesort([1,3,4,2,5])