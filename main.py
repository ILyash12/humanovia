class Human:
	def __init__(self, name):
		self.name = name
		self.gladness = 100
	def live(self):
		print(self.name, 'is alive')
	def eat(self):
		print('Eating time')

class Teacher(Human):
	def live(self):
		super().live()
		print('What a wonderful day of', self.name)
	def teach(self):
		print(self.name, 'is teaching')
        self.gladness -= 20


class Student(Human):
	def __init__(self, name):
		super().__init__(name)
	def study(self):
		print(self.name, 'is studying')
		self.gladness -= 20

human = Human('Bob')
human.live()
t1 = Woman('Clara')
t1.live()
t1.teach()
st1 = Man('John')
st1.live()
st1.study()