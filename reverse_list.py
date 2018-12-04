import time
import random
import statistics

def create_array(num):
    array = []
    for x in range(num):
        array.append(random.randint(1,101))
    return array

def reverse_array_timing(array):
    start = time.time()
    array.reverse()
    end = time.time()
    return(end - start)

num = 50000
timings = []
for x in range(20):
    array = create_array(num)
    timings.append(reverse_array_timing(array))
    duration = statistics.median(timings)
    print('{}\t{}'.format(len(array), duration))
    num += 50000
