import time
import random
import statistics

def create_array(num):
    array = list(range(0, num))
    return array

def shuffle_array_timing(array):
    start = time.time()
    random.shuffle(array)
    end = time.time()
    return(end - start)

num = 10000
timings = []
for x in range(20):
    array = create_array(num)
    for x in range(100):
        timings.append(shuffle_array_timing(array))
    duration = statistics.median(timings)
    print('{}\t{}'.format(len(array), duration))
    num += 10000
