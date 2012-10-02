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
