# Inheritance vs Composition
# More architectural question:
# When should one class inherit from another, and when should it contain another object?
print()
print("Inheritance vs Composition")
print()

# Inheritance
# is-a relationship

# Animal
# ├── Dog
# └── Cat

class Animal:
    def speak(self):
        sound = "Some sound"
        return sound

class Dog(Animal): #Dog inherits from Animal
    pass

dog = Dog() #dog is an instance of class object Dog

# Conceptually we think this as
# Dog inherits Animal
# So, Animal.speak(dog)
# Dog is an Animal (inheritance based on is-a relationship)

print()
print(dog.speak)
print(dog.speak())

# Composition
# Car does not inherit from Engine
# Car contains an Engine object 
# Car has an Engine (composition based on has-a relationship)

# Car
# ├── Engine
# ├── Battery
# ├── Wheels
# └── ...

class Engine:
    def start(self):
        # print("Engine started")
        engine_state = "Engine Started"
        return engine_state

class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()

print()
print(car.engine.start)
print(car.engine.start())

# Another Example

# Phone class
#    ↓
# phone instance
#    │
#    └── battery → Battery instance
#                     │
#                     └── charge()



class Battery:
    def charge(self):
        # print("Charging")
        charge_state = "Charging"
        return charge_state

class Phone:
    def __init__(self):
        # self.battery is instance of Battery()
        # Battery() creates a new Battery instance, 
        # and that instance is stored in the phone object's battery attribute
        self.battery = Battery()

phone = Phone()
print()
print(phone.battery)
print(phone.battery.charge)

# phone [is a phone instance]
#   ↓
# .battery [retrieves its battery instance attribute]
#   ↓
# .charge() [retrieves and calls the charge method on that Battery instance]

print(phone.battery.charge())

# When designing a class, ask:
# “Is this thing a specialized version of that thing?”
# → Consider inheritance.
# “Does this thing contain/use another thing?”
# → Consider composition.


# And in real-world software engineering, 
# composition is often preferred over inheritance when both could work, 
# because it generally gives you more flexible and less tightly coupled designs.