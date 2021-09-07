class Dog:
    def __init__(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name


def func(dog: Dog):
    dog = Dog("wwwww")
    print(dog.getName())


if __name__ == '__main__':
    dog = Dog("www");
    func(dog)
    print(dog.getName())

