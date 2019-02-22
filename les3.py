import math, sys, os, re
#EASY 1
#var 1 
print('*' * 100)
print('EASY #1 task VAR 1')
def var1(n, nd):
    n=n*(10**nd)+0.41
    n = n//1
    return n/(10**nd)

print(var1(2.123124141, 5))


#var 2
print('*' * 100)
print('EASY #1 task VAR 2')
def var2(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree
print(var2(3.1234567, 5))


#EASY 2
print('*' * 100)
print('EASY #2 task')
def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last

print(lucky_ticket(112211))
print(lucky_ticket(121122))


#hard 1
print('*' * 100)
print('HARD #1 task')
def search1(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
def search2(a, b):
    return a * b / search1(a, b)
def diff(lst):
    difference = lst[0]
    for x in range(len(lst)):
        if x:
            difference = difference - lst[x]
    return difference
def forms1(num, NOK):
    if num > NOK:
        cel = num // NOK
        new_num = num % NOK
        result = '{0:.0f} {1:.0f}/{2:.0f}'.format(cel, new_num, NOK)
    else:
        result = '{0:.0f}/{1:.0f}'.format(num, NOK)
    return result

equation = '7/17 - -5'
params = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
funcs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
nums = []
noms = []
i = 0
for param in params:
    temp = param.split('/')
    nums.append(int(temp[0]))
    if len(temp) > 1:
        noms.append(int(temp[1]))
    else:
        noms.append(1)
for p in funcs:
    if p:
        func = p.strip()
        break
NOK = search1(noms[0], noms[1])
for n in nums:
    nums[i] = n * NOK / noms[i]
    i += 1
print('result ' + equation + ':')
if func == '+':
    print(forms1(sum(nums), NOK))
elif func == '-':
    print(forms1(diff(nums), NOK))
else:
    print('No')

print('*' * 100)
print('NORMAL #1 task')
def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(5, 10)
#