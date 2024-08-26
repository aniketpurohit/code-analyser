# data_class.py


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age} years old, from {self.city}"


if __name__ == "__main__":
    person = Person("Alice", 30, "New York")
    print(person)
