from multiprocessing import Pool
import math

def hard_math(number):
    return math.factorial(number)

pool = Pool(10)

freeze_support()
print pool.map(hard_math, range(1,2))