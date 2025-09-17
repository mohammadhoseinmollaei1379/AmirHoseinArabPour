class Dog:
    species = "canis"
    def __init__(self, name, age, species):
        self.sound = "woof!"
        self.name = name
        self.age = age
        self.species = species
    def bark(self):
        print(self.sound)

dog_dog = Dog("dog", 2, "body")

print(
    "sound : ", dog_dog.sound,
    "name : ", dog_dog.name,
    "age : ", dog_dog.age,
    "feature : ", dog_dog.species
)




