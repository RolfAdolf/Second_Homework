import sys

from task_2 import largest_number
from task_2_rough import largest_number as largest_number_rough

rough = False

if len(sys.argv) > 0:
    rough = True if sys.argv[0]=='rough' else False

if (rough):
    print(largest_number_rough(input(), input()))
else:
    print(largest_number(input(), input()))