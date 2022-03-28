import os
import json


class Config:
	def __init__(self, path: str):
		if type(path) is not str:
			path = str(path)

		self.__path = path
		self.__data = {}


	def get(self, key: str):
		if key in self.__data:
			return self.__data[key]
		else:
			return None


	def set(self, key: str, value):
		self.__data[key] = value


	def delete(self, key: str) -> bool:
		if key in self.__data:
			del self.__data[key]
			return True
		else:
			return False


	def get_keys(self) -> list:
		return self.__data.keys()


	def dump(self) -> str:
		return json.dumps(self.__data, indent=4, sort_keys=True)


	def wipe(self):
		self.__data = {}


	def __len__(self):
		return len(self.__data)


	def __contains__(self, key: str):
		return key in self.__data


	def __getitem__(self, key: str):
		return self.get(key)


	def __setitem__(self, key: str, value):
		self.set(key, value)


	def __delitem__(self, key: str):
		self.delete(key)


	def read_file(self, load_if_corrupt = False):
		f = self.__get_config_file()

		file_data = f.read()

		if len(file_data) <= 0:
			file_data = "{}"
		
		try:
			self.__data = json.loads(file_data)
		except ValueError as e:
			if not load_if_corrupt:
				raise ValueError("Configuration file " + self.__path + " appears to be corrupt!")
			else:
				self.__data = {}

		f.close()


	def write_file(self):
		f = self.__get_config_file("w")

		f.write(self.dump())

		f.close()


	def __get_config_file(self, mode: str = "r"):
		if len(self.__path) <= 0 or self.__path.endswith(os.path.sep) or os.path.isdir(self.__path):
			raise OSError("Invalid configuration file path: " + self.__path)

		if not os.path.exists(self.__path):
			file_dir = os.path.dirname(self.__path)
			if not os.path.exists(file_dir):
				os.makedirs(file_dir)
			open(self.__path, "w").close()
			
		return open(self.__path, mode)
