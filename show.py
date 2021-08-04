import json 

class Show:
	""" Show class """
	__SHOWS = list()
	__SHOW_NAMES = list()
	__STATUS = ["watched", "watchlist", "watching"]
	__WATCHED = list()
	__WATCHING = list()
	__WATCHLIST = list()

	def __init__(self, name, status):
		"""  Init method """
		if not isinstance(name, str):
			raise TypeError("Wrong data type")

		elif name in Show.__SHOW_NAMES:
			raise ValueError("Already added")

		self.name = name

		if status not in Show.__STATUS:
			raise ValueError("Unallowed state")

		self.status = status.lower()
		self.__classify()
		Show.__SHOWS.append(self.__dict__)
		Show.__SHOW_NAMES.append(self.name)

		with open('shows.json', 'r+') as file:
			file_data = json.load(file)
			if self.__dict__ in file_data['shows']:
				pass 
			else:
				file_data['shows'].append(self.__dict__)
				file.seek(0)
				json.dump(file_data, file, indent=4)

	def __classify(self):
		""" Classifies shows based on status """
		if self.status == "watched":
			Show.__WATCHED.append(self.name)
			with open('watched.json', 'r+') as file:
				file_data = json.load(file)
				if self.name in file_data['watched']:
					pass 
				else:
					file_data['watched'].append(self.name)
					file.seek(0)
					json.dump(file_data, file, indent=4)


		elif self.status == "watchlist":
			Show.__WATCHLIST.append(self.name)
			with open('watchlist.json', 'r+') as file:
				file_data = json.load(file)
				if self.name in file_data['watchlist']:
					pass 
				else:
					file_data['watchlist'].append(self.name)
					file.seek(0)
					json.dump(file_data, file, indent=4)


		else:
			Show.__WATCHING.append(self.name)
			with open('watching.json', 'r+') as file:
				file_data = json.load(file)
				if self.name in file_data['watching']:
					pass 
				else:
					file_data['watching'].append(self.name)
					file.seek(0)
					json.dump(file_data, file, indent=4)

	def __str__(self):
		""" triggered when used print func"""
		return f"{self.name}:{self.status}"

	def __repr__(self):
		""" representation of Show object"""
		return f"({self.name}, {self.status})"

	def showList(self):
		""" show list """
		print("Show list")
		for i, k in enumerate(Show.__SHOWS, 1):
			print(i, k)
		print('  ')

	def shows(self):
		"""shows """
		print("Shows:")
		for i, j in enumerate(Show.__SHOW_NAMES, 1):
			print(i, j)
		print('  ')

	def watching(self):
		""" watching shows"""
		print("Shows watching currently:")
		for i, j in enumerate(Show.__WATCHING, 1):
			print(i, j)
		print('  ')

	def watched(self):
		""" watched shows"""
		print("Watched shows:")
		for i, j in enumerate(Show.__WATCHED, 1):
			print(i, j)
		print('  ')

	def watchlist(self):
		""" watchlist shows"""
		print("Watchlist:")
		for i, j in enumerate(Show.__WATCHLIST, 1):
			print(i, j)
		print('  ')
