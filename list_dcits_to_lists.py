from multiprocessing import Pool
import math

def hard_math(number):
    return math.factorial(number)

pool = Pool(10)

print pool.map(hard_math, range(1,101))