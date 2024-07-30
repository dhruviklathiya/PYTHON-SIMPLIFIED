# Time taken for list Vs. generator
# For finding how much memory is taken by both we must run this code with

import time

t1 = time.time()
_list = [i for i in range(0,100000000)]
# _list = [i for i in range(0,1000000000)] # Do not uncomment this if you have low speed processor
print(f"Taken time by list: {time.time() - t1}")

t1 = time.time()
_generator_object = (i for i in range(0,100000000))
t2 = time.time()
print(f"Taken time by generator: {time.time() - t1}")
print(f"Output is {int(time.time() - t1)} because of negative exponential")