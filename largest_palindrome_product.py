import math
import time
def isPalindrome(n):
    copy = n
    rev = 0
    while(copy):
        rev *= 10
        rev += copy%10
        copy = copy//10
    if rev == n:
        return True
    return False

##Brute Force
start = time.time()
max = 0
x = 0
y = 0
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j):
            if i*j > max:
                max = i*j
                x = i
                y = j
end = time.time()
prev = end-start
print(x*y, prev)

##Optimized Approach, roughly 10 times faster
new_s= time.time()
max = 0
a = 999
while(a>100):
    b = 990
    while(b>100):
        val = a*b
        if isPalindrome(val):
            if val > max:
                max = val
        b -= 11
    a -= 1
new_e = time.time()
curr = new_e-new_s
print(max, curr)
print(prev/curr)
