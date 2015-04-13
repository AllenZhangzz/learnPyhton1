#encoding:utf-8

# def hello():
# 	print 'Hello, everybody!\nNice to see you!'
# hello()

# def printMax(a,b):
# 	if a>b:
# 		print a,'is maximun'
# 	else :
# 		print b,'is maximun'
# printMax(9,9.4)

# s=9
# r=8
# printMax(s,r)

def func():
	global aa
	aa= 99
	print aa
func()

aa=4
func()