# Class = blueprint
# Object = actual thing the blueprint creates

# # What is an object?
# i.e. dog object adjectives/attributes: legs, ears, eyes, fur, weight
# i.e. dog object verbs/actions: bark, wag tail, eat, sleep
# 
# Class name starts with Capital letter
# Must have constructor method: __init__(self)
# Constructor runs automatically when the Class is called; all other methods in class need to be called to run
#
# The self variable is talking about that specific object (like "this" in JS) 

class Dog:  # blueprint of dog; not actual dog
    def __init__(self, name, hair, weight):  # constructor method: a method is a function built into a class
        self.legs = 4  # hard-coded attributes that the user can't change
        self.ears = 2
        self.eyes = 2
        self.name = name  # user chooses the name
        self.hair = hair  # user chooses what type of hair the dog has
        self.weight = weight

    def wagTail(self):  # every method requires self parameter, but no argument for self is need when calling the method
        print("the dog is wagging its tail")
    
    def growl(self):
        print('Grrrrrrrrrrrrrrrr')

    def eat(self, amount):
        self.weight += amount  # using self. so it only targets one dog object, not all of them

    def makeWaste(self):
        self.weight -= 1

    def intro(self):
        print("My name is", self.name)

dog1 = Dog("Mac", "black and tan", 80)  # instanciating a dog (creating actual dog from blueprint)
dog2 = Dog("Jaxson", "chocolate", 75)  # the instance being creating is stored in the variable
print(dog1)  # prints memory address; each object has a different memory address
print(dog2)
print(dog1.name)  # prints Mac
print(dog2.weight)  # prints 75 lbs
# dot notation: no () for attributes; () for methods
dog1.wagTail()
dog2.growl()
print(dog1.weight)  # 80 pounds
dog1.eat(1)  # Mac ate 1 lb of of food
print(dog1.weight)  # Mac now weighs 81 lbs
dog1.makeWaste()  # Mac poops
print(dog1.weight)  # Mac now weighs 80 lbs
dog1.intro()
dog2.intro()