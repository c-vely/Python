'''
# test 1
import calculate

s = calculate.add(2, 3)
print(s) # 5

s = calculate.mul(3, 5)
print(s) # 15


# test 2
from calculate import add

s = add(2, 3) 
print(s) # 5

s = mul(3, 5) # NameError: name 'mul' is not defined


# test 3
from calculate import add, mul

s = add(2, 3) 
print(s) # 5

s = mul(3, 5) 
print(s) # 15


# test 4
from calculate import *

s = add(2, 3) 
print(s) # 5

s = mul(3, 5) 
print(s) # 15


'''
# test 5 : 별명 사용
import calculate as cal

s = cal.add(2, 3)
print(s) # 5
