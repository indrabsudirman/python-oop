class Student:
    # Create initializer for Student class
    def __init__(self, name, age, major):
        self.name = name
        self.age = age  
        self.major = major

    # vars(object) is a built-in function that returns a dictionary containing all attributes (properties) of an object.
    def __str__(self):
        return str(vars(self))

# Create instance of Student class
Indra = Student("Indra", 20, "Math")
# Print instance variables
print(Indra)