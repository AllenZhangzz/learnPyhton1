# -*- coding:utf-8 -*-
__author__ = 'Allen'

'Class Learing'

# class Student(object):
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age

# 	def print_age(self):
# 		print self.age 
# 	def print_name(self):
# 		pass
# ss=Student('SDfsdf',23)

# ss.print_age()

class Student(object):
	"""docstring for Student"""
	def __init__(self,name,age):
		# super(Student, self).__init__()
		self._name = name
		self._age = age
	
	def get_name(self):
		return self._name
	def get_age(self):
		return self._age

	def set_name(self,sttt):
		# if not isinstance(sttt,str):
		# 	raise ValueError('Name is not ......')
		self._name = sttt

	def set_age(self,value):
		if not isinstance(value,int):
			raise ValueError('Age must be an integer!')
		if value <0 or value > 130:
			raise ValueError('Age must between 0~130')
		self._age = value

stu = Student()

stu.get_name()
stu.get_age()






