from math import *
import sys
sys.set_int_max_str_digits(8000)
sys.setrecursionlimit(10000)
F2024_to_F2023 = 2 * 2024
F2023_to_F2022 = 2 * 2022
a = (F2024_to_F2023  / 16) - 1
b = F2023_to_F2022
print(a/b)