#    Main Author(s): Sheida Hashem Dabbaghian
#    Main Reviewer(s): Kage Gamis

class HashTable:
	class Node:
		# A node class for the linked list used in chaining.
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.next = None

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	def __init__(self, cap=32):
		# Set the initial capacity of the hash table
		self._capacity = cap
		self.table = [None] * self._capacity
		self.size = 0 # Initialize the size of the table

	def hash_function(self, key):
		# python hash() function and modulo operation
		return hash(key) % self._capacity

	def insert(self,key, value): # Insert a new key-value pair into the hash table
		if self.search(key):
			# If the key already exists, do not insert and return False
			return False
		
		index = self.hash_function(key) # Compute the index for the key using the hash function
		new_node = self.Node(key, value) # Create a new node with the key and value

		if self.table[index] is None:
			# If the slot at the computed index is empty, place the new node there
			self.table[index] = new_node

		else:
			# If a collision occurs, use chaining to add the node to the end of the linked list
			current = self.table[index]
			while current.next:
				current = current.next

			current.next = new_node

		self.size += 1 # Increment the size of the table
		if self.size / self._capacity > 0.7: # Check if resizing is needed (load factor exceeds 0.7)
			self.resize()

		return True


	
	# Modify the value of an existing key
	def modify(self, key, value):
		index = self.hash_function(key)
		# Start at the head of the linked list at the index
		current = self.table[index]

		# Traverse the linked list to find the matching key
		while current:
			if current.key == key:
				# Update the value and return True
				current.value = value
				return True
			current = current.next
		return False # If key is not found, return False

	
	# Remove a key-value pair from the hash table
	def remove(self, key):
		index = self.hash_function(key)
		# Start at the head of the linked list at the index
		current = self.table[index]
		prev = None

		while current:
			# Traverse the linked list to find the matching key
			if current.key == key:
				if prev is None:
					# If the node to remove is the head, update the head
					self.table[index] = current.next
				else:
					prev.next = current.next
				self.size -= 1 # Decrement the size of the table
				return True
			prev = current
			# Move to the next node in the list
			current = current.next
		return False # If key is not found, return False
		

	def search(self, key):
		# Search for a key in the hash table
		index = self.hash_function(key)
		# Start at the head of the linked list at the index
		current = self.table[index]

		while current:
			# Traverse the linked list to find the matching key
			if current.key == key:
				# Return the value if the key is found
				return current.value
			current = current.next
		return None # If key is not found, return None
		

	def capacity(self): # Get the capacity (number of slots) of the hash table
		return self._capacity
		

	def __len__(self):
		# Get the number of key-value pairs stored in the table
		return self.size

	def resize(self):
		# Resize the hash table when the load factor exceeds 0.7
		old_table = self.table # Save the old table
		self._capacity *= 2 # Double the capacity
		self.table = [None] * self._capacity # Create a new table with the updated capacity
		self.size = 0 # Reset the size

		# Insert again all nodes from the old table into the new table
		for node in old_table:
			current = node
			while current:
				self.insert(current.key, current.value)
				current = current.next
		

