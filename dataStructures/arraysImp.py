import mem_profile

print('Memory usage (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

# implement dynamic array
from array import *

simpleArray = array('i', [1, 2, 4, 5])
print(simpleArray[1])

print('Memory usage (After): {}Mb'.format(mem_profile.memory_usage_resource()))
