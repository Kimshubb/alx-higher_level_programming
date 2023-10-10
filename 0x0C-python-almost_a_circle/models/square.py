#!/usr/bin/python3
from models.rectangle import rectangle
'''Class square defination that inherits from rectangle because it is a 
   special rectangle
 '''
class Square(Rectangle):
	'''class quare defination'''
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)
	
	def __str__():
		return f"[Square]({self.id}) {self.x}/{self.y} - {self.width}"
	@property
	def size(self):
		'''getter method for the size attribute'''
		return self.width
	@size.setter
	def size(self, value):
		'''setter method for the size attribute'''
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		if args:
			attributes = ["id", "size", "x", "y"]
			for attribute, value in zip(attributes, args):
				setattr(self, attribute, value)
			elif kwargs:
				for key, value in kwargs,item():
					setattr(self, key, value)
