import math

# Standard recursive fibonacci
# no optimizations
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

# Memoize: remember results from previous function output
# This is a simple memoize function for functions with one argument.
# Can instead wrap with functools.lru_cache()
def memoize(f):
    global memo
    memo = {}
    def memoized(x):
        if x not in memo:
            value = f(x)
            memo[x] = value
            return value
        return memo[x]
    return memoized

## Mandelbrot Set
# Recursive Mandelbrot
def mandelbrot(z, c, n):
    if n > 100:
        return n
    elif abs(z) >= 2:
        return n
    return mandelbrot(z**2 + c, c, n+1)

# Generator Mandelbrot
def mandel(c):
    z = 0+0j
    while abs(z) <= 2:
        yield pow(z, 2) + c
        z = pow(z, 2) + c

# Wrap the mandel() function to determine whether an item is in or is not in the Mandelbrot set
def is_mandel(c, max_iter=100):
    for i, z in enumerate(mandel(c)):
        if i > max_iter:
            return True
    else:
        return False

# Wrap the mandel() function to count the iterations
def mandel_iters(c, max_iter=100):
    for i, z in enumerate(mandel(c)):
        if i > max_iter: # set a cutoff. it takes longer and longer to see the divergence as you get closer
            return i-1
    else:
        return i-1

# Recursive function to generate Pascal's triangle
def pascal(c, r):
    # Base case
    if c == 0 or c == r or r == 1:
        return 1
    # inductive step
    else:
        return pascal(c, r-1) + pascal(c-1, r-1)

# Print out Pascal's Triangle
def print_pascal():
    for r in range(10):
        for c in range(r+1):
            # TODO: center-justify based on max range.
            print('{} '.format(pascal(c, r)), end='')
        print()

# Recursion for solving the problem:
# How many ways to make change from a given dollar value?
def make_change(value, coins=(0.01, 0.05, 0.10, 0.25, 0.50)):
    # Base case: success
    if math.isclose(value, 0, abs_tol=1e-6): # handle floating point precision issues
        return 1
    # Base case: faliure
    elif len(coins) == 0 or value < 0:
        return 0
    else:
        # Inductive step
        return make_change(value - coins[0], coins) \
                + make_change(value, coins[1:])

# Recursive Data Structures
# Node: an element of a Linked list
class Node():
    def __init__(self, value, _next):
        self.value = value
        self._next = _next

    def __iter__(self):
        return self

    def __next__(self):
        return self._next

# LinkedList: helper functions around a chain of Nodes
# Technically, a Node itself is a linked list! This just wraps
# the set of Node objects
class LinkedList():
    def __init__(self, iterable):
        self.head = Node(iterable[0], None)
        curr = self.head
        for item in iterable[1:]:
            curr._next = Node(item, None)
            curr = curr._next
        self.tail = self.head._next
    def __iter__(self):
        return self

    # Exhaust the linked list.
    # This isn't really what we want to do,
    # because we lose the data!
    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            value = self.head.value
            self.head = self.tail
            try:
                self.tail = self.head._next
            except:
                self.tail = None
            return value

    # Use a generator to iterate through linkedlist values
    def _iterate(self):
        head = self.head
        tail = self.tail
        while head is not None:
            yield head
            head = tail
            tail = head._next if head is not None else None

    # return the index of a value, else -1 if not in list
    def find(self, item):
        for i, node in enumerate(self._iterate()):
            if node.value == item:
                return i
        else:
            return -1

    def print_list_iter(self):
        print('|',end='')
        print(', '.join(str(value) for value in self), end='')
        print('|') # newline

    def print_list_gen(self):
        print('|',end='')
        print(', '.join(str(n.value) for n in self._iterate()), end='')
        print('|') # newline

def main():
    print("Make Change Demo")
    print()
    print("making change...")
    print('0.05 => ', make_change(0.05))
    print('0.10 => ', make_change(0.10))
    print('1.00 => ', make_change(1.00))
    print()
    print("Pascal's Triangle:")
    print_pascal()
    print()
    print("Linked List")
    print("making a linked list from range(5)")
    L = LinkedList(range(5))
    print("print_list_gen()")
    L.print_list_gen()
    print()
    print("L.find(2)")
    print('L.find(2) = ', L.find(2))

if __name__ == '__main__':
    main()