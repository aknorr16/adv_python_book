# Simple examples
for i in [1, 2, 3, 4]:
    print i

for letter in "DataScience":
    print letter

# iter function

x = iter([1, 2, 3])
x.next()
x.next()
x.next()

# once we run out of lines in the list StopIteration is raised as an error. This cannot be iterated through agian.

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


test = yrange(4)

test.next()
test.next()

# iter benefits

from sys import getsizeof

my_comp = list(range(1000))
my_iter = iter(range(1000))

print(getsizeof(my_comp))
print(getsizeof(my_iter))

