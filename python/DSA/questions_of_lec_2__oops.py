# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length 
#         self.width = width 

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

#     def __str__(self):
#         return f" Length: ({self.length} , Width:  {self.width})" 
    

# class Square(Rectangle):
#     def __init__(self, length):
#         super() .__init__(length,length)

#     def __str__(self):
#         return "Square: " + super().__str__()
    





# r = Rectangle(2,2)
# print(r)
# print(r.area())
# print(r.perimeter())


# s = Square(2)
# print(s.area())
# print(s.perimeter())




#================================================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age= age

#     def __str__(self):
#         return f"(Name: , {self.name} , Age: , {self.age})"
    

# class Doctor(Person):
#     def __init__(self, name , age , specialization):
#         super() .__init__(name , age)
#         self.specialization = specialization

#     def __str__(self):
#         return f"Doctor {super().__str__()} , Specialization in: {self.specialization}"
    


# class Patient(Person):
#     def __init__(self, name, age ,disease):
#         super() . __init__(name , age)
#         self.disease = disease

#     def __str__(self):
#         return f"Patient {super().__str__()} , Disease: {self.disease}"
    


# P = Person("Sania" , 37)
# print (P)

# d = Doctor( "Ali" , 40 , "Cardiologist")
# print(d)

# p = Patient("Sara" , 25 , "Flu")
# print(p)




#===========================================



# class Staff:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return f"Name:{self.name}  Salary:{self.salary}"



# class Nurse(Staff):
#     def __init__(self, name, salary, shift ):
#         super() .__init__(name, salary)
#         self.shift = shift

#     def __str__(self):
#         return f"Shift:{self.shift}"
    


# class Surgeon(Staff):
#     def __init__(self, name , salary ,operations_performed):
#         super() .__init__(name, salary)
#         self.operations_performed = operations_performed

    
#     def __str__(self):
#         return f"Operation Performed by Surgeon:  # {self.operations_performed} "
    

# s = Staff("Zunaira" , 3500)
# print(s)


# n = Nurse("Sara" , 1500 , "Morning")
# print(n)

# n2= Nurse("Summaiya" , 1500 , "Night")
# print(n2)


# S = Surgeon("Hafsa" , 250000 , 9)
# print(S)







#--------------------------------Encapsulation Examples------------------------

#============================================
# class BankAccount:
#     def _init_(self, title, balance):
#         self.title = title
#         self.__balance = balance

#     def deposit(self, amount):
#         if(amount > 0):
#             self.__balance += amount
#         else:
#             print("Ghareeb")

#     def withdraw(self, amount):
#         if(amount < self.__balance):
#             self.__balance -= amount;
#         else:
#             print("Aukaat mai")

#     def balance(self):
#         return self.__balance
    
# acc1 = BankAccount("Hafsa", 1000)
# acc1.deposit(500) #1500
# acc1.withdraw(1000) #500
# print(acc1.balance()) #500




#---------------------------------------------------------------------



# Create a Student class with:
# A private attribute __grade.
# A set_grade() method that only allows grades between 0 and 100.
# A get_grade() method that returns the grade.
# 👉 Task: Create an object and try setting valid and invalid grades.



# class Student:
#     def __init__(self, grade=0):
#         self.__grade = grade

#     def set_grade(self, marks):
#         if(marks > 0 and marks <= 100):
#             self.__grade += marks
#             print ("valid grade")

#         else:
#             print("Invalid grade")

#     def get_grade(self):
#         return self.__grade
    



    
# s1 = Student(82)
# s1.set_grade(20)
# print(s1.get_grade())

# s2 = Student()
# s2.set_grade(101)
# print(s2.get_grade())













#---------------------




# Q3. Property Decorators
# Create a Car class with:
# A private attribute __speed.
# Use @property to get the speed.
# Use @speed.setter to set the speed, but only if it’s between 0 and 200.
# 👉 Task: Try setting the speed to 150 (works) and 300 (should print an error)





# class Car:
#     def _init_(self, speed=0):
#         self.__speed = speed
    
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, newSpeed):
#         if(newSpeed > 1 and newSpeed <= 150):
#             self.__speed = newSpeed
#         else:
#             print("Speed is too high. Marjayega")
# s1 = Car()
# s1.speed = 50
# print(s1.speed)
#---------------------------









    



# Q4. Employee Salary (Encapsulation without @property)
# Create a class Employee with:
# A private attribute __salary.
# A method set_salary(amount) that only sets the salary
#  if it’s greater than 20,000 and less than 200,000.
# A method get_salary() that returns the salary.
# 👉 Task:
# Create an employee with a starting salary of 30,000.
# Try to set their salary to 15,000 (should fail)
# Then set it to 50,000 (should succeed).
# Print the final salary.

# class Employee:
#     def _init_(self, salary = 0):
#         self.__salary = salary

#     def set_salary(self, amount):
#         if(amount >= 20000 and amount <= 200000):
#             self.__salary = amount
#         else:
#             print("Not an ideal salary")

#     def get_salary(self):
#         return self.__salary

# e1 = Employee()
# e1.set_salary(30000)
# print(e1.get_salary())
# e2 = Employee()
# e2.set_salary(15000)
# print(e2.get_salary())








#============================================================================
# Q1. Single Inheritance
# Create a class Vehicle with a method move().
# Create a class Car that inherits from Vehicle and has its own method fuel_type().
# 👉 Task: Create a Car object, call both methods.
# Q2. Multiple Inheritance
# Create two classes:
# Teacher with a method teach().
# Athlete with a method play().
# Create a class Person that inherits from both.
# 👉 Task: Show that Person can both teach() and play().
# Q3. Multilevel Inheritance
# Create a class Grandparent with a method legacy().
# Create Parent (inherits Grandparent) with a method work().
# Create Child (inherits Parent) with a method study().
# 👉 Task: Show that Child can access methods from all 3 levels.
# Q4. Hierarchical Inheritance
# Create a class Shape with a method area().
# Create two child classes: Circle and Square, both inheriting from Shape.
# 👉 Task: Demonstrate that both Circle and Square can access area(), but implement it differently.



#------------------------

# Q1. Single Inheritance
# Create a class Vehicle with a method move().
# Create a class Car that inherits from Vehicle and has its own method fuel_type().


# class Vehicle:

#     def __init__(self):
#         pass 

#     def move(self):
#         print("Vehicle is moving")


# class Car(Vehicle):
#     def __init__(self):
#         pass

#     def fuel_type(self):
#         print("Car is moving")



# c = Car()
# print(c.move())
# print(c.fuel_type())



#--------------------------------------------------------------------
# Q2. Multiple Inheritance
# Create two classes:
# Teacher with a method teach().
# Athlete with a method play().
# Create a class Person that inherits from both.
# 👉 Task: Show that Person can both teach() and play().



# class Teacher:
#     def __init__(self):
#         pass

#     def teach(self):
#         print("teach")


# class Athlete:
#     def __init__(self):
#         pass


#     def play(self):
#         print("Athlete")



# class Person(Teacher,Athlete ):
#      def __init__(self):
#          pass
     
#      def teach(self):
#          return super().teach()
     
#      def play(self):
#          return super().play()
     

# p = Person()
# print(p.teach())
# print(p.play())

     


#--------------------------------------------------------------
# Q3. Multilevel Inheritance
# Create a class Grandparent with a method legacy().
# Create Parent (inherits Grandparent) with a method work().
# Create Child (inherits Parent) with a method study().
# 👉 Task: Show that Child can access methods from all 3 levels.



# class Grandparent:
#     def __init__(self):
#         pass

#     def legacy(self):
#         # print("Legacy")
#         return "Legacy" 

    
# class Parent(Grandparent):
#     def __init__(self):
#         pass

#     def work(self):
#         return "Work"


# class Child(Parent):
#     def __init__(self):
#         pass

#     def Study(self):
#         return "Study"




# c = Child()
# print(c.legacy())
# print(c.work())
# print(c.Study())



    

#--------------------------------------------------------
# Q4. Hierarchical Inheritance
# Create a class Shape with a method area().
# Create two child classes: Circle and Square, both inheriting from Shape.
# 👉 Task: Demonstrate that both Circle and Square can access area(), but implement it differently.


# class Shape:
#     def __init__(self):
#         pass

#     def area(self):
#         return "Area"
    


# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return f"Area of circle: {self.radius * self.radius * 3.142} "
    



# class Square (Shape):
#     def __init__(self,length):
#         self.length = length

#     def area(self):
#         return f"Area of square: {self.length * self.length }"
    


# c = Circle(2)
# print(c.area())

# s = Square(4)
# print(s.area())



#-----------------------------------------Abstraction 
# from abc import ABC, abstractmethod

# class Animal:
#     def _init_(self):
#         pass

#     @abstractmethod
#     def make_sound(self):
#         pass
    
# class Dog(Animal):
#     def _init_(self):
#         pass

#     def make_sound(self):
#         return f"Dogesh bhai bhonka"
    
# class Cat(Animal):
#     def _init_(self):
#         pass

#     def make_sound(self):
#         return f"Billi boli"
    
# dogeshBhai = Dog()
# print(dogeshBhai.make_sound())
# billiShapater = Cat()
# print(billiShapater.make_sound())


#--------------------------------------------------------------------------------------
#Q2
# Q. Vehicle (Abstraction)
# Create an abstract class Vehicle with abstract methods:
# start_engine()
# stop_engine()
# Then create two subclasses:
# Car → implement methods with "Car engine started" / "Car engine stopped".
# Bike → implement methods with "Bike engine started" / "Bike engine stopped".
# 👉 Task:
# Try to instantiate Vehicle (should give error).
# Create objects of Car and Bike and call their methods.

# from abc import ABC, abstractmethod


# class Vehicle(ABC):
     
    
#     def __init__(self):
#      pass


#     @abstractmethod
#     def start_engine(self):
#       return "Start Engine"
     

#     @abstractmethod
#     def stop_engine(self):
#        return "Stop Engine()"
     


# class Car(Vehicle):
#    def __init__(self):
#      pass
   


#    def start_engine(self):
#       return "Car engine started"
   

    
#    def stop_engine(self):
#       return "Car engine stopped"
   



# class Bike(Vehicle):
#  def __init__(self):
#     pass
  
#  def start_engine(self):
#       return "Bike engine started"
   

    
#  def stop_engine(self):
#       return "Bike engine stopped"
    



# v = Vehicle()
# print(v.start_engine())
# print(v.stop_engine())


# c = Car()
# print(c.start_engine())
# print(c.stop_engine())


# b = Bike()
# print(b.start_engine())
# print(b.stop_engine())




















#------------------------------------------------again inheritance















# # Q4. Employee Salary (Encapsulation without @property)
# # Create a class Employee with:
# # A private attribute __salary.
# # A method set_salary(amount) that only sets the salary
# #  if it’s greater than 20,000 and less than 200,000.
# # A method get_salary() that returns the salary.
# # 👉 Task:
# # Create an employee with a starting salary of 30,000.
# # Try to set their salary to 15,000 (should fail)
# # Then set it to 50,000 (should succeed).
# # Print the final salary.

# class Employee:
#     def __init__(self, salary= 0):
#         self.__salary = salary 

#     def set_salary(self, amount):
#         if (amount > 20000 and amount <= 200000):
#            self.__salary += amount

#         else:
#             print("Error")

#     def get_salary(self):
#         return self.__salary
    

# e = Employee()
# e.set_salary(300000)
# print(e.get_salary())




# class Person:
#     def _init_(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)

# class Student(Person):  # inherits from Person
#     def _init_(self, name, student_id):
#         super()._init_(name)  # 👈 call parent constructor
#         self.student_id = student_id

#     def show(self):
#         super().show()  # use parent’s method
#         print("ID:", self.student_id)

# # Usage


# s1 = Student("Hafsa", 101)
# print(s1.show())





# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length 
#         self.width = width 

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

#     def __str__(self):
#         return f" Length: ({self.length} , Width:  {self.width})" 
    

# class Square(Rectangle):
#     def __init__(self, length):
#         super() .__init__(length,length)

#     def __str__(self):
#         return "Square: " + super().__str__()
    





# r = Rectangle(2,2)
# print(r)
# print(r.area())
# print(r.perimeter())


# s = Square(2)
# print(s.area())
# print(s.perimeter())






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age= age

#     def __str__(self):
#         return f"(Name: , {self.name} , Age: , {self.age})"
    

# class Doctor(Person):
#     def __init__(self, name , age , specialization):
#         super() .__init__(name , age)
#         self.specialization = specialization

#     def __str__(self):
#         return f"Doctor {super().__str__()} , Specialization in: {self.specialization}"
    


# class Patient(Person):
#     def __init__(self, name, age ,disease):
#         super() . __init__(name , age)
#         self.disease = disease

#     def __str__(self):
#         return f"Patient {super().__str__()} , Disease: {self.disease}"
    


# P = Person("Sania" , 37)
# print (P)

# d = Doctor( "Ali" , 40 , "Cardiology")
# print(d)

# p = Patient("Sara" , 25 , "Flu")
# print(p)








class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name:{self.name}  Salary:{self.salary}"



class Nurse(Staff):
    def __init__(self, name, salary, shift ):
        super() .__init__(name, salary)
        self.shift = shift

    def __str__(self):
        return f"Shift:{self.shift}"
    


class Surgeon(Staff):
    def __init__(self, name , salary ,operations_performed):
        super() .__init__(name, salary)
        self.operations_performed = operations_performed

    
    def __str__(self):
        return f"Operation Performed by Surgeon:  # {self.operations_performed} "
    

s = Staff("Zunaira" , 3500)
print(s)


n = Nurse("Sara" , 1500 , "Morning")
print(n)

n2= Nurse("Summaiya" , 1500 , "Night")
print(n2)


S = Surgeon("Hafsa" , 250000 , 9)
print(S)



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Hafsa", 95)

# print(s1.name)   # direct access
# print(s1.marks)  # direct access

class Student:
    def __init__(self, name, age):
        self.__name = name     # Private
        self.__age = age       # Private
    
    # Getter method (sirf value lene ke liye)
    def get_name(self):
        return self.__name
    
    # Setter method (sirf value change karne ke liye)
    def set_age(self, new_age):
        if new_age > 0:         # condition check
            self.__age = new_age
        else:
            print("Invalid age")

s1 = Student("Ali", 20)
print(s1.get_name())    # Ali
s1.set_age(25)          # age change ho gayi



#----------------------------------------------------------------------------

class Student :
    def __init__(self,name,age,gender,height):
        self.__name = name 
        self.__age = age
        self.__gender = gender 
        self.__height = height 

    def get_name(self):
        return self


