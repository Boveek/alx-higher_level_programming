#!/usr/bin/python3
""" A class represenation """


from models.base import Base
class Rectangle(Base):
	def __init__(self, width, height, x=0, y=0, id=None):
		if type(width) is not int:
			raise TypeError("width must be an integer")
		if width <= 0:
			raise ValueError("width must be > 0")
		self.__width = width
		if type(height) is not int:
			raise TypeError("height must be an integer")
		if height <= 0:
			raise ValueError("height must be > 0")
		self.__height = height
		if type(x) is not int:
			raise TypeError("x must be an integer")
		if x < 0:
			raise ValueError("x must be >= 0")
		self.__x = x
		if type(y) is not int:
			raise TypeError("y must be an integer")
		if y < 0:
			raise ValueError("y must be >= 0")
		self.__y = y
		super().__init__(id)

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if type(value) is not int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		if type(value) is not int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

	def area(self):
		return self.__height * self.__width

	def display(self):
		for i in range(self.__y):
			print()
		for i in range(self.__height):
			print(" " * self.__x + "#" * self.__width)

	def __str__(self):
		return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

	def update(self, *args, **kwargs):
		if args:
			if len(args) >= 1:
				self.id = args[0]
			if len(args) >= 2:
				self.__width = args[1]
			if len(args) >= 3:
				self.__height = args[2]
			if len(args) >= 4:
				self.__x = args[3]
			if len(args) >= 5:
				self.__y = args[4]
		else:
			if 'id' in kwargs:
				self.id = kwargs['id']
			if 'width' in kwargs:
				self.__width = kwargs['width']
			if 'height' in kwargs:
				self.__height = kwargs['height']
			if 'x' in kwargs:
				self.__x = kwargs['x']
			if 'y' in kwargs:
				self.__y = kwargs['y']
	def to_dictionary(self):
		"""
		Returns a dictionary representation of the Rectangle instance.
		"""
		return {
			'id': self.id,
			'width': self.__width,
			'height': self.__height,
			'x': self.__x,
			'y': self.__y
			}
