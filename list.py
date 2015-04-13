# encoding utf-8

#a = []
# a= range(91)
# print a[-5:]
# print a[20:]

# str = 'Allen Zhang'
# str1 = ('Allen Zhang','Alex Li','Yang Shan')
# print str[::3]
# print str1[2]

# --Iteration--

# from	collections import Iterable

# atuple = ('Allen Zhang','Alex Li','Yang Shan')

# print isinstance(atuple,Iterable)

# for i,value in enumerate(atuple):
# 	print i, value

# for value in enumerate(atuple):
# 	print  value

# for a,b,c in [(1,2,3),(2,3,3),(3,44,44)]:
# 	print a+b+c


# l =[]
# for x in range(2,11):
# 	l.append(x^2*x)
# print l

# aa=[a+'+'+b+'+'+c for a in 'spqr' for b in '4xyzu' for c in '231']
# print aa

# # --Generator--
# aa=(a+'+'+b+'+'+c for a in 'spqr' for b in '4xyzu' for c in '231')
# for b in aa:
# 	print b[::2]

# for aa in (a+'+'+b+'+'+c for a in 'spqr' for b in '4xyzu' for c in '231'):
# 	print aa
from cmath import sqrt
def is_prime(n):
	list_num = []
	for i in range(2, n):
		for num in range(2, int(sqrt(n))+1):
			if i % num == 0 and i != num:
				break
			elif i % num != 0 and num == (int(sqrt(n))):
				list_num.append(i)
			return list_num
print is_prime(9)



