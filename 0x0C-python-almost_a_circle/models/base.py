#!/usr/bin/python3
""" A class representation """
import json
import csv


class Base:
	""" A representation of the base of our OOP hierarchy"""

	__nb_objects = 0
	def __init__(self, id=None):
		""" Instancialize constructor"""
		if id == None:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
		else:
			self.id = id

	@staticmethod
	def to_json_string(list_dictionaries):
		""" Jsonifies a dictionary so it's quite rightly and longer"""
		if list_dictionaries is None or list_dictionaries == []:
			return []
		return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		""" Saves jsonified object to file"""
		filename = cls.__name__ + ".json"
		with open(filename, "w") as jsonfile:
			if list_objs is None:
				jsonfile.write("[]")
			else:
				list_dicts = [o.to_dictionary() for o in list_objs]
				jsonfile.write(Base.to_json_string(list_dicts))

	@staticmethod
	def from_json_string(json_string):
		""" Unjsonifies a dictionary"""
		if json_string is None or json_string == "[]":
			return []
		return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		""" Loads instance from dictionary"""
		if dictionary and dictionary != {}:
			if cls.__name__ == "Rectangle":
				new = cls(1, 1)
			else:
				new = cls(1)
		new.update(**dictionary)
		return new

	@classmethod
	def load_from_file(cls):
		""" Loads object to csv file"""
		filename = str(cls.__name__) + ".json"
		try:
			with open(filename, "r") as jsonfile:
				list_dicts = Base.from_json_string(jsonfile.read())
				return [cls.create(**d) for d in list_dicts]
		except IOError:
			return []

	@classmethod
	def save_to_file_csv(cls, list_objs):
		""" Saves object to csv file"""
		filename = cls.__name__ + ".csv"
		with open(filename, "w", newline="") as csvfile:
			if list_objs is None or list_objs == []:
				csvfile.write("[]")
			else:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					for obj in list_objs:
						writer.writerow(obj.to_dictionary())

	@classmethod
	def load_from_file_csv(cls):
		""" Loads object to csv file"""
		filename = cls.__name__ + ".csv"
		try:
			with open(filename, "r", newline="") as csvfile:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
					list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
					list_dicts = [dict([k, int(v)] for k, v in d.items())
						for d in list_dicts]
					return [cls.create(**d) for d in list_dicts]
		except IOError:
				return []
