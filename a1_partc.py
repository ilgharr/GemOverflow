#    Main Author(s): Ilghar Rahno 137542213
#    Main Reviewer(s): Renato Cordova
from itertools import count


class Stack:
    """
    Stack represents a last-in, first-out (LIFO) data structure.
    """

    def __init__(self, cap=10):
        """
        Initializes the Stack with a specified capacity.

        Parameters:
        cap (int): The initial capacity of the stack (default is 10).

        Raises:
        IndexError: If the provided capacity is less than 1.
        """
        if cap < 1:
            raise IndexError('Can not have less than 1 index in a stack!')
        self.cap = cap
        self.stack = [None] * cap
        self.top = -1
        self.count = 0

    def capacity(self):
        """
        Returns the current capacity of the stack.
        """
        return self.cap

    def double(self):
        """
        Doubles the capacity of the stack and copies the elements to the new stack.
        This allows pushing new elements when the stack is full.
        """
        self.cap *= 2
        new_stack = [None] * self.cap
        for i in range(self.count):
            new_stack[i] = self.stack[i]
        self.stack = new_stack

    def push(self, data):
        """
        Pushes a new element onto the top of the stack.

        Parameters:
        data: The data to be pushed onto the stack.

        This method automatically doubles the stack capacity if needed.
        """
        if self.count + 1 > self.cap:
            self.double()
        self.stack[self.count] = data
        self.count += 1
        self.top += 1

    def pop(self):
        """
        Pops the top element from the stack and returns it.

        Returns:
        The data that was at the top of the stack.

        Raises:
        IndexError: If the stack is empty.
        """
        if self.count == 0:
            raise IndexError('pop() used on empty stack')
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        self.count -= 1
        return data

    def get_top(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
        The data at the top of the stack.
        """
        return self.stack[self.top]

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return self.count == 0

    def __len__(self):
        """
        Returns the number of elements in the stack.
        """
        return self.count


class Queue:
    """
    Queue represents a circular queue, which is a first-in, first-out (FIFO) data structure.
    """

    def __init__(self, cap=10):
        """
        Initializes the Queue with a specified capacity.

        Parameters:
        cap (int): The initial capacity of the queue (default is 10).

        Raises:
        IndexError: If the provided capacity is less than 1.
        """
        if cap < 1:
            raise IndexError('Can not have less than 1 index in a queue!')
        self.cap = cap
        self.queue = [None] * cap
        self.front = 0
        self.rear = -1
        self.count = 0

    def capacity(self):
        """
        Returns the current capacity of the queue.
        """
        return self.cap

    def double(self):
        """
        Doubles the capacity of the queue and rearranges the elements.
        This allows enqueuing new elements when the queue is full.
        """
        new_cap = self.cap * 2
        new_queue = [None] * new_cap
        for i in range(self.count):
            new_queue[i] = self.queue[(self.front + i) % self.cap]
        self.cap = new_cap
        self.queue = new_queue
        # Reset front and rear positions to start from zero.
        self.front = 0
        self.rear = self.count - 1

    def enqueue(self, data):
        """
        Adds an element to the rear of the queue.

        Parameters:
        data: The data to be added to the queue.

        This method automatically doubles the queue capacity if needed.
        """
        if self.count == self.cap:
            self.double()
        self.count += 1
        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = data

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Returns:
        The data that was at the front of the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        if self.count == 0:
            raise IndexError('dequeue() used on empty queue')
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.count -= 1
        return data

    def get_front(self):
        """
        Returns the front element of the queue without removing it.

        Returns:
        The data at the front of the queue, or None if the queue is empty.
        """
        if self.count == 0:
            return None
        return self.queue[self.front]

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return self.count == 0

    def __len__(self):
        """
        Returns the number of elements in the queue.
        """
        return self.count


class Deque:
    """
    Deque represents a double-ended queue (Deque), which allows insertion and removal from both ends.
    """

    def __init__(self, cap=10):
        """
        Initializes the Deque with a specified capacity.

        Parameters:
        cap (int): The initial capacity of the deque (default is 10).

        Raises:
        IndexError: If the provided capacity is less than 1.
        """
        if cap < 1:
            raise IndexError('Can not have less than 1 index in a queue!')
        self.cap = cap
        self.queue = [None] * cap
        self.front = 0
        self.rear = -1
        self.count = 0

    def capacity(self):
        """
        Returns the current capacity of the deque.
        """
        return self.cap

    def double(self):
        """
        Doubles the capacity of the deque and rearranges the elements.
        This allows pushing new elements when the deque is full.
        """
        new_cap = self.cap * 2
        new_queue = [None] * new_cap
        for i in range(self.count):
            new_queue[i] = self.queue[(self.front + i) % self.cap]
        self.cap = new_cap
        self.queue = new_queue
        # Reset front and rear positions to start from zero.
        self.front = 0
        self.rear = self.count - 1

    def push_front(self, data):
        """
        Adds an element to the front of the deque.

        Parameters:
        data: The data to be added to the front.

        This method automatically doubles the deque capacity if needed.
        """
        if self.count == self.cap:
            self.double()
        self.count += 1
        self.front = (self.front - 1) % self.cap
        self.queue[self.front] = data

    def push_back(self, data):
        """
        Adds an element to the rear of the deque.

        Parameters:
        data: The data to be added to the rear.

        This method automatically doubles the deque capacity if needed.
        """
        if self.count == self.cap:
            self.double()
        self.count += 1
        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = data

    def pop_front(self):
        """
        Removes and returns the front element of the deque.

        Returns:
        The data that was at the front of the deque.

        Raises:
        IndexError: If the deque is empty.
        """
        if self.count == 0:
            raise IndexError('pop_front() used on empty deque')
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.count -= 1
        return data

    def pop_back(self):
        """
        Removes and returns the rear element of the deque.

        Returns:
        The data that was at the rear of the deque.

        Raises:
        IndexError: If the deque is empty.
        """
        if self.count == 0:
            raise IndexError('pop_back() used on empty deque')
        data = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear = (self.rear - 1) % self.cap
        self.count -= 1
        return data

    def get_front(self):
        """
        Returns the front element of the deque without removing it.

        Returns:
        The data at the front of the deque, or None if the deque is empty.
        """
        if self.count == 0:
            return None
        return self.queue[self.front]

    def get_back(self):
        """
        Returns the rear element of the deque without removing it.

        Returns:
        The data at the rear of the deque, or None if the deque is empty.
        """
        if self.count == 0:
            return None
        return self.queue[self.rear]

    def is_empty(self):
        """
        Checks if the deque is empty.

        Returns:
        True if the deque is empty, False otherwise.
        """
        return self.count == 0

    def __len__(self):
        """
        Returns the number of elements in the deque.
        """
        return self.count

    def __getitem__(self, k):
        """
        Returns the element at index k, counting from the front.

        Parameters:
        k (int): The index of the element to retrieve.

        Returns:
        The element at index k.

        Raises:
        IndexError: If the index is out of range.
        """
        if k < 0 or k >= self.count:
            raise IndexError('Index out of range')
        return self.queue[(self.front + k) % self.cap]