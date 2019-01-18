## Approach 1
# c = {}
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n not in c:
#         c[n] = fib(n-1) + fib(n-2)
#     return c[n]
# n = 1
# sum = 0
# val = 0
# while val <= 4000000:
#     if val%2 == 0:
#         sum += val
#     n += 1
#     val = fib(n)
# print(sum)

## Approach 2
# x = y = 1
# sum = 0
# while x <= 4000000 and y <= 4000000:
#     sum += (x+y)
#     x,y = x + 2*y, 2*x + 3*y
# print(sum)

## Apprach 3
golden_ratio = 1.618
c = golden_ratio**3
sum = 0
num = 2
while(num < 4000000):
    sum += num
    num = num * c
print(sum)
