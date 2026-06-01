import math
import struct
import random
import time

def fast_inv_sqrt(number):
    threehalfs = 1.5

    x2 = number * 0.5
    y = number

    i = struct.unpack('i', struct.pack('f', y))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('f', struct.pack('i', i))[0]

    y = y * (threehalfs - (x2 * y * y))
    return y

# Datos de prueba
N = 1_000_000
nums = [random.uniform(0.1, 1000.0) for _ in range(N)]

# math.sqrt
t0 = time.perf_counter()
s = 0.0
for x in nums:
    s += math.sqrt(x)
t1 = time.perf_counter()

print("math.sqrt:", t1 - t0)

# Fast inverse sqrt
t0 = time.perf_counter()
s2 = 0.0
for x in nums:
    s2 += fast_inv_sqrt(x)
t1 = time.perf_counter()

print("fast_inv_sqrt:", t1 - t0)