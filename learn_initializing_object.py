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

class Teacher:
    def __init__(self, name = None, age = None, subject = None):
        self.name = name
        self.age = age
        self.subject = subject
    def __str__(self):
        return str(vars(self))

# Create instance of Teacher with default values
Bayu = Teacher()
# Print instance variables
print(Bayu)
Ibayu = Teacher("Ibayu", 20, "Math")
print(Ibayu)