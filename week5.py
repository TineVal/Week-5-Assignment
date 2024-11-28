#Assignment One
class Book:
    def __init__(self, name, size):
        self.name= name
        self.size = size
    
    def show(self):
        print(f'This book is {self.size} sized and it is called {self.name}')

class Novel(Book):
    def __init__(self, name, size, type):
        super().__init__(name, size)
        self.type = type

    def show(self):
        print(f'This is a {self.type} book called {self.name}')
    

b = Book("Twighlight", "middle")
b.show()
n = Novel("Dark Lady", "middle", "crime thriller")
n.show()

#Assignment Two
class Vehicles:
    def __init__(self, name):
        self.name = name

class Car:
    def move(self):
        print("Drive")

class Plane:
    def move(self):
        print("Fly")

class Boat:
    def move(self):
        print("Float")

c = Car
c.move("Self")
p = Plane
p.move("Self")
B = Boat
B.move("Self")



        