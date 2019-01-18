# sum = 0
# for i in range(1000):
#     if i%3 == 0 or i%5 == 0:
#         sum += i
# print(sum)

##Approach using Sum of Arithmetic series Formula
max = 999
threes_n = max//3
fives_n = max//5
fifteens_n = max//15
threes = (threes_n/2)*(2*3+(threes_n-1)*3)
fives  = (fives_n/2)*(2*5+(fives_n-1)*5)
fifteens = (fifteens_n/2)*(2*15+(fifteens_n-1)*15)

print(threes+fives-fifteens)
