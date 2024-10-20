import math

def string_times(str, n) -> str:
    """
    https://codingbat.com/prob/p193507
    
    """
    return str * n

def front_times(str, n) -> str:
    """
    https://codingbat.com/prob/p165097
    """
    return n * str[:3] if len(str) >= 3 else n * str

def array_count9(nums) -> int:
    """
    https://codingbat.com/prob/p166170
    """
    count = 0
    for element in nums:
        if element == 9:
            count += 1
    return count

def array_front9(nums) -> bool:
    """
    https://codingbat.com/prob/p110166
    """
    return 9 in nums[:4]

def array123(nums) -> bool:
    """
    https://codingbat.com/prob/p193604
    """
    if len(nums) < 3:
        return False
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

def string_match(a, b) -> int:
    """
    https://codingbat.com/prob/p182414
    """
    count = 0
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
    for i in range(len(short) - 1):
        if short[i] == long[i] and short[i + 1] == long[i + 1]:
            count += 1
    return count

def first_half(str) -> str:
    """
    https://codingbat.com/prob/p107010
    """
    return str[:len(str) // 2]

def without_end(str) -> str:
    """
    https://codingbat.com/prob/p138533
    """
    return str[1:-1]

def combo_string(a, b) -> str:
    """
    https://codingbat.com/prob/p194053
    """
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
    return short + long + short

def left2(str) -> str:
    """
    https://codingbat.com/prob/p160545
    """
    return str[2:] + str[:2]

def near_ten(num) -> bool:
    """
    https://codingbat.com/prob/p165321
    """
    return num % 10 <= 2 or num % 10 >= 8

def count_code(str) -> int:
    """
    https://codingbat.com/prob/p186048
    """
    count = 0
    for i in range(len(str) - 3):
        if str[i] == 'c' and str [i + 1] == 'o' and str[i + 3] == 'e':
            count += 1
    return count


def end_other(a, b) -> bool:
    """
    https://codingbat.com/prob/p174314
    """
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

def centered_average(nums):
    """
    https://codingbat.com/prob/p126968
    """
    nums.sort()
    if len(nums) % 2 != 0:
        return int(nums[len(nums) // 2])
    return int((nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2)

"""
https://www.cs.toronto.edu/~guerzhoy/180/midterm/mt2022/paper.pdf#page=7

Write a function that, when called, returns the next digit of Ï€ (approx 3.14159...). You may assume that
the function will not be called more than 10 times.

The function would be used like this:

print(next_digit_pi()) # 3
print(next_digit_pi()) # 1
print(next_digit_pi()) # 4
print(next_digit_pi()) # 1

You may import math and use math.pi
"""

# Define any additional global variables here
ptr = 0

def next_digit_pi():
    global ptr
    pi_str = str(math.pi).replace(".", "")[ptr]
    ptr += 1
    return pi_str

if __name__ == "__main__":
    print(next_digit_pi())
    print(next_digit_pi())
    print(next_digit_pi())
    print(next_digit_pi())
