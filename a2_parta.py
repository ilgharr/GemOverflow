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

	def hash_function(self, key):
		return hash(key) % self._capacity

	def insert(self,key, value):
		if self.search(key) is not None:
			return False

		index = self.hash_function(key)
		new_node = self.Node(key, value)

		if self.table[index] is None:
			self.table[index] = new_node

		else:
			current = self.table[index]
			while current.next is not None:
				current = current.next

			current.next = new_node

		self.size += 1
		if self.size / self._capacity > 0.7:
			self.resize()

		return True



	def modify(self, key, value):
		index = self.hash_function(key)
		current = self.table[index]

		while current is not None:
			if current.key == key:
				current.value = value
				return True
			current = current.next
		return False


	def remove(self, key):
		index = self.hash_function(key)
		current = self.table[index]
		prev = None

		while current is not None:
			if current.key == key:
				if prev is None:
					self.table[index] = current.next
				else:
					prev.next = current.next
				self.size -= 1
				return True
			prev = current
			current = current.next
		return False
		

	def search(self, key):
		index = self.hash_function(key)
		current = self.table[index]

		while current is not None:
			if current.key == key:
				return current.value
			current = current.next
		return None
		

	def capacity(self):
		return self._capacity
		

	def __len__(self):
		return self.size

	def resize(self):
		old_table = self.table
		self._capacity *= 2
		self.table = [None] * self._capacity
		self.size = 0

		for node in old_table:
			current = node
			while current is not None:
				self.insert(current.key, current.value)
				current = current.next
		

