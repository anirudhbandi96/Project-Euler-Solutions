import math
import time
def is_prime(integer):
    """Returns True if input is a prime number"""
    if integer < 2:  # remove long if using Python 3
        return False
    if integer == 2:
        return True
    if integer % 2 == 0: # which can also be written as -> if not integer & 1:
        return False
    for divisor in range(3, int(math.sqrt(integer)) + 1, 2):
        if integer % divisor == 0:
            return False
    return True
def nth_prime_number(n):
    count = 0
    num = 0
    while(count<n):
        num += 1
        if is_prime(num):
            count += 1
    return num
start = time.time()
print(nth_prime_number(10001))
end = time.time()
print(end-start)
