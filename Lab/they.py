class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    
    def __str__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, gender={self.gender}, age={self.age})"
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def set_first_name(self,first_name):
        self.first_name = first_name

    def set_last_name(self,last_name):
        self.last_name = last_name

    def set_gender(self,gender):
        self.gender = gender

    def set_age(self,age):
        self.age = age

    def age_up(self):
        self.age += 1

Person1 = Person(
    first_name="John",
    last_name="Doe",
    gender="Male",
    age=30
)

Person2 = Person(
    first_name="Jane",
    last_name="Smith",
    gender="Female",
    age=25
)

print(Person1)
Person1.age_up()

print(Person1)