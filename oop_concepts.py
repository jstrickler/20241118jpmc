colors = list()   # list colors = new list();
colors.append('red')
colors.append('orange')
colors.insert(0, "green")

dogs = list()
dogs.append("Rin-tin-tin")
dogs.append("Benjy")

class Animal:
    pass

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d = Dog()
d.bark()