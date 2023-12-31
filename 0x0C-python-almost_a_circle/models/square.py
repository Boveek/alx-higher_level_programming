#!/usr/bin/python3
""" A class representation """
from models.rectangle import Rectangle


class Square(Rectangle):
	""" A sqaure class"""

	def __init__(self, size, x=0, y=0, id=None):
		""" Instatialisation constructor"""
		super().__init__(size, size, x, y, id)

	def __str__(self):
		""" Returns string info about this square"""
		return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

	@property
	def size(self):
		""" Size of the square"""
		return self.height

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		"""
		Assigns attributes based on *args and **kwargs.
		*args: List of arguments (id, size, x, y)
		**kwargs: Keyworded arguments (id=id, size=size, x=x, y=y)
		"""
		if args:
			if len(args) >= 1:
				self.id = args[0]
			if len(args) >= 2:
				self.size = args[1]
			if len(args) >= 3:
				self.x = args[2]
			if len(args) >= 4:
				self.y = args[3]
		else:
			if 'id' in kwargs:
				self.id = kwargs['id']
			if 'size' in kwargs:
				self.size = kwargs['size']
			if 'x' in kwargs:
				self.x = kwargs['x']
			if 'y' in kwargs:
				self.y = kwargs['y']

	def to_dictionary(self):
		"""
		Returns a dictionary representation of the Square instance
		"""
		return {
			'id': self.id,
			'size': self.size,
			'x': self.x,
			'y': self.y
			}
