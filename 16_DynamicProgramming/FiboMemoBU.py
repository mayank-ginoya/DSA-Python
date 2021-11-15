import timeit


def FiboTab(n):
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[:n]

print(timeit.timeit('FiboTab(10)',number=100,globals=globals()))
print(timeit.timeit('FiboTab(20)',number=100,globals=globals()))
print(timeit.timeit('FiboTab(100)',number=100,globals=globals()))