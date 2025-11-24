class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, birth_year, current_year):
        age = current_year - birth_year
        return cls("Rex", age)

    def __str__(self):
        return f"{self.name}, {self.age} years old"



dog1 = Dog.from_birth_year(2018, 21111)  
print(dog1) 