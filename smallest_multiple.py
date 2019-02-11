from functools import reduce
digits = [20,19,18,17,16,15,14,13,12,11]
n = 1
print(reduce(lambda x,y: x*y, digits))
while(True):
    # print(n)
    flag = True
    for i in digits:
        if n%i != 0:
            flag = False
            break
    if flag:
        print(n)
        break
    else:
        n += 1
