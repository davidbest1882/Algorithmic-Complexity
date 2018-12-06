# colours = ['red', 'orange', 'red', 'yellow', 'green', 'blue', 'indigo', 'green', 'red', 'violet']
import time
import random
import statistics
from random_word import RandomWords

# def find_duplicate(list):
#     duplicates = set()
#     for item in range(len(list)):
#         word = list.pop()
#         for item in list:
#             if word == item:
#                 if word not in duplicates:
#                     duplicates.append(word)
#     return duplicates
def find_duplicate(array):
    seen = set()
    dup = set()
    for x in array:
        if x not in seen:
            seen.add(x)
        else:
            dup.add(x)
    return(dup)

def find_duplicates(list):
    array = list
    duplicates = []
    unique = []
    for word in array:
        if word not in unique:
            unique.append(word)
        else:
            if word not in duplicates:
                duplicates.append(word)
    return duplicates

# if not find_duplicate([1,2,3]) == []:
#     raise Exception('Test 1 failed')
#
# if not find_duplicate([1,2,2]) == [2]:
#     raise Exception('Test 2 failed')

def create_array(size):
    r = RandomWords()
    array = []
    for x in range(10):
        array += (r.get_random_words(limit=size))
    return(array)

def find_duplicates_timing(array):
    start = time.time()
    find_duplicate(array)
    end = time.time()
    return(end - start)

timings = []
array = []
new_arr = []
for x in range(20):
    array += (create_array(50))
    # array = create_array(num)
    for x in range(50):
        new_arr = array[:]
        timings.append(find_duplicates_timing(new_arr))
    duration = statistics.median(timings)
    print('{}\t{}'.format(len(array), duration))
