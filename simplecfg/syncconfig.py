from simplecfg.config import Config


class SynchronousConfig(Config):
	def __init__(self, path: str):
		super().__init__(path)


	def set(self, key: str, value):
		super().set(key, value)
		self.write_file()


	def delete(self, key: str) -> bool:
		result = super().delete(key)
		self.write_file()
		return result


	def wipe(self):
		super().wipe()
		self.write_file()