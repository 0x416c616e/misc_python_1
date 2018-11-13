# Python object-oriented programming

class Employee:
	def __init__(self, first, last, pay): 	#sorta like a constructor
											#instance should be called self
											#think "this" in java
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + last + '@example.com'
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)

print("hello")

#emp_1.first = 'Corey'
#emp_1.last = 'Schafer'
#emp_1.email = 'coreyschafer@example.com'
#emp_1.pay = 50000


#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'testuser@example.com'
#emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)


#print(emp_1.fullname())
print(Employee.fullname(emp_1))
#print(emp_1.fullname())

