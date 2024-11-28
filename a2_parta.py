#    Main Author(s): Sheida Hashem Dabbaghian
#    Main Reviewer(s):

class HashTable:
	class Node:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.next = None

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	def __init__(self, cap=32):
		self._capacity = cap
		self.table = [None] * self._capacity
		self.size = 0

	def insert(self,key, value):
		pass

	def modify(self, key, value):
		pass

	def remove(self, key):
		pass

	def search(self, key):
		pass

	def capacity(self):
		pass

	def __len__(self):
		pass

