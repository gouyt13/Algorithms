import bisect
import os 
import sys 

py_path = sys.argv[0]
py_dir = os.path.dirname(py_path)
filename = "2sum.txt"
filepath = os.path.join(py_dir, filename)

num_set = set()
with open(filepath) as file:
    for num in file.readlines():
        num = int(num)
        num_set.add(num)

num_list = sorted(num_set)
targets = set()
for num in num_list:
    low = bisect.bisect_left(num_list, -10000-num)
    high = bisect.bisect_right(num_list, 10000-num)
    for num_2 in num_list[low:high]:
        if num_2 != num:
            targets.add(num+num_2)

print(len(targets))