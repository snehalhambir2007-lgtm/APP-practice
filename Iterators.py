class Numbers:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i <= self.n:
            x = self.i
            self.i += 1
            return x
        else:
            raise StopIteration

# Main Program
num = int(input("Enter a number: "))

for i in Numbers(num):
    print(i)
