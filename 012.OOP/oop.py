class MyClass:
    """This is documentation
    Describe something about this class"""

    a = 10
    name = "Tom"
    def func(self):
        print("Hi!", self.name)

#Output: 10
print(MyClass.a)

#Output: This is documentation
#        Describe something about this class
print(MyClass.__doc__)

# MyClass.func()
# MyClass.func() missing 1 required positional argument: 'self'

# need to create an instance of MyClass
obj = MyClass()
obj.func()

class Parrot:
    """doc"""
    # instance attributes
    def __init__(self, name, age):
        self.name   = name
        self.age    = age

    #instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

# instantine the obj
blu = Parrot("Kuro", 10)

print(blu.sing("\"I like Blue\""))

# parent class
class Anime:
    def __init__(self):
        print("Anime is not cartoon.")
    def whutisThis(self):
        print("Anime dayo.")
    def watch(self):
        print("SFW only.")
    def whatepisode(self):
        print("All of \'em.")
# child class
class MHA(Anime):
    def __init__(self):
        # AttributeError: 'MHA' object has no attribute 'whatepisode'
        # no super init :))
        # Base().__init__(self)
        # https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
        super().__init__() # to call the parent class.
        print("MHA is Boku no Hiro not Boku no piko.")
    def whutisThis(self):
        print("My hero academia is mid.")
    def watch(self):
        print("Deku get reckt.")

ani = Anime()
mha = MHA()

mha.whutisThis()
mha.whatepisode()

# Multiple Inheritance:
#       Multi derived
#       Multi level inheritance

# MRO: method resolution order
# <child class>.mro()

class A1: pass
class A2: pass
class A3: pass
class A4: pass

class B1(A1, A2): pass
class B2(A3, A2): pass

class obj(B1, B2, A4): pass

print(B2.mro(), '\n', obj.mro())

# Encapsulation
# use _ or __ to make something private

# why dont we use __ for const
class Constant:
    def __init__(self):
        __pii = 3.14159265
        __aho = "bakayarou"

    # def __<> # create an private Function

constant = Constant()
# may be the name too long or too inconvinient?

# Polymorphism
#   override
#   many class have the same func
