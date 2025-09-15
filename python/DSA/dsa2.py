# ++++++++++ OOPS IN PYTHON -----------------------------------
# WHAT ARE DUNDER FUNCTIONS?
# These are ====> Double underscore functions
# -------> They are used in constructors when we set parameters

# yani OOPs mai jo hamare constructor bante hain unme class ka name nahi aata
# balki __init__ aata hai.

# C# mai jo (this) ===> instance ka kaam karta tha
# yaha wo kaam (self) keyword karta hai.


class Python:
    def __init__(self, x=0, y=9):
        self.x = x
        self.y = y


# now here we create the object of class Python
# here p1 is ("reference variable") yani
# aisa variable jisme object ko store kiya jaye  *Like a pointer*
p1 = Python()
print("P1 = ", p1)

p2 = Python(2, 4)
print("P2 = ", p2)


# |||||||||||||||||||....... CASTING .........|||||||||||||||||||||

# below there is a function that perform casting  
# ok now here casting means conversion of data types like:
# int --> string
# string --> int and so on....
def __get_human_readable__(self):
    return "[" + str(self.x) + "," + str(self.y) + "]"


# Another dunder function:
# string representation of the object return karta hai ye function
def __str__(self):
    return "[" + str(self.x) + "," + str(self.y) + "]"


# ////////////////////////////////////////////////////////////////////////////////////////


# # class bana rahe hain
# class Student:
#     # constructor (ye auto call hota hai jab object banta hai)
#     def __init__(self, name, age):
#         self.name = name   # self ka matlab current object
#         self.age = age

#     # method (function jo class ke andar hota hai)
#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def new(self):
#         print("Her name is ", self.name)
#         print("Her age is ", self.age)


# # main part (yaha object banayenge)
# s1 = Student("Hafsa", 19)   # object banaya aur constructor call hua
# s1.show()                   # method call
# s1.new()
# # above line is the object and the main work of upper class Student 


# ^^^^^^^^^^^^^ ANOTHER EXAMPLE OF CASTING ^^^^^^^^^^^^^^^^^
x = "30"     # ---> this is string
y = int(x)   # -----> that string convert in to integer and stored in the variable (y)
print(y + 5)  # ---> 35


# ^^^^^^^^^^^^^ ANOTHER EXAMPLE OF CASTING ^^^^^^^^^^^^^^^^^
a = 100          # integer
b = str(a)       # int → string
print("Number is " + b)   # output: Number is 100




#.........................................................................................







#Another Important thing here is :
# jb c# mai ham constructor bnaty thy tw aksar constructor chaining mai hm brackets lgaky khali chordety thy like this :
# { }  but python ma aysa nahi ha ❌❌❌ ulta yaha ye scene ha bhe ky 
# _____________________ yha hamhye body mai [PASS] likhna houta hai kuky agr kuch ni likha tw wo error houga just because hm 
#brakets nhi lgaty python mai islye ham [PASS] likhty hn colon ky bd (:)
#_____________________PASS basically ---> (NOPE OPERATION) ----> that means body hai python ka mou bnd houjyga ab 😈😈😈😈




#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000



#now here one more imp concept 
#there is a code :


def __intit__(self, x = 0 , y = 0):
    self.x = x
    self.y = y

def __init__(self):
    pass 

def __str__(self):
    return "[" + str(self.x) + ":" + str(self.y) + "]"


# now lets concentrate here :::: IN PYTHON THERE IS NO CONCEPT OF OVERLOADING 
# MEANSSS----->   
        # agr mainy aik def function k nechy dosra def function bnaya ha tw uper wala yani 
        #phela wala function khtm houjyga wo run nai houga cuzzzzz
        #   IN PYTHON THERE IS NO CONCEPT OF OVERLOADING 
        # wo (OVER---WRITING)✅ hougaa not OVER RIDING❌





#ab ik or chez is line mai ye ky 
    return "[" + str(self.x) + ":" + str(self.y) + "]"
# yaha mainy str ky parenthesis mai (self.x)  islye likha ha kuky 
#kuky python mai is rule ko  kha jata ha 
                #  [EXPLICIT OVER IMPLICIT]
 




#fields ham aam taur py constructor k andr bnaty hen 
#python ma ye tareeqa nh houta k phely sy initialize
#  kiya jaye kuky yha py explicit declaration nh ha














#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#_____________________________________________[COMPOSITION]____________________________________________________________________
              #         MEANS IK CLASS KY ANDR KISI OR CLASS KA INSTANCE RKHNA HAI
# Basically bht sari chezo ko mila k ik bari class compose krni houti ha


# class Shape:
#     def __init__(self, points):
#         self.points = points
    
#     def __str__(self):
#         ret = " "
        

#         for i in self.points:
#             ret += str(i) + " - "

#         return ret
    

# #object work of (main) below

# p1 = Point(5, 5)
# p2 = Point(10, 5)
# p3 = Point(5, 10)
# p = [p1 , p2 , p3]



# sh = Shape (p)
# print (sh)












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Correct code acc to vs
class Point:
    def __init__(self, x, y):   # Point class ka constructor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"   # jab Point ko print karenge to x,y dikhayega

class Shape:
    def __init__(self, points):   
        self.points = points
    
    def __str__(self):
        ret = ""

        for i in self.points:
            ret += str(i) + " - "   # har point ko string mai convert karega aur join karega

        return ret
    
# objects bana rahe hain
p1 = Point(5, 5)
p2 = Point(10, 5)
p3 = Point(5, 10)

p = [p1, p2, p3]   # ek list jisme tino points hain


sh = Shape(p)     # Shape class ka object, jisme points diye
print(sh)         # Shape ka __str__ call hoga

#one more imp concept ham :
# python mai ik class bnanay k bd sary objects, functions bnanay k bd bi
#  mazeed  bd mai functions add krskty hen ---> thats called --> (MONKEY PATCHING)

def print_points(self):
    for i in self.points:
        print(i)    
Shape.print_points = print_points
sh.print_points()       





#________________________________________________________[INHERITANCE]____________----------------------------
#continue = skip current iteration
#pass = do nothing, just placeholder

#--------Inheritance:

class Triangle(Shape):
    pass

t = Triangle(p)
t.print_points()









#_________________________________________________________________________________________________________________________________________________________________________
# now here the point is that jistrh hm c# mai virtual and override keywords use krty thy idhr aysa scene nhi ha
# yha parenthesis ky andr jis class ko inherit krna houta ha wo likhdi jati ha faltu mai keywords and priv wgera use nh kra jata
# Override karna ho to sirf same method ka naam likh do child class me,
#  Python khud samajh leta hai ke ye parent ka method replace (override) kar raha hai.

 # simple example:
class Animal:
    def speak(self):
        print("Animal is speaking")
                             
class Cat(Animal):
    def speak(self): # Method override, keyword ki zarurat nahi
        print("Cat meow")

c = Cat()
c.speak()




#===========================================================below part smjh nhi aya bahrh ma jaye...

def get_area(self):
    vertices = self.points
    n = len(vertices) #ye count karega kitne points hain (triangle ke case me 3).
    a = 0.0  #ye ek temporary variable hai jisme hum formula ka result step by step add karenge.

    for i in range(n):
         j = (i + 1) % n
         a += (vertices[i].x * vertices[j].y) - (vertices[j].x * vertices[i].y)
    return abs(a) / 2.0


#yahaan trick hai 👇
# i = current point index
# j = next point index
# % n ka matlab hai agar last point pe ho to wapas first point le lo (wrap around).
#.........................................................................................
# example agar 3 points hain:
# i=0 → j=1
# i=1 → j=2
# i=2 → j=0 ✅ (wapas first point)

Triangle.get_area = get_area
print(t.get_area())



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#^^^^^^^^^^^^^^^^^          New Topic
#simple code
class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return "L: " + str(self.length) + " W: " + str(self.width)


r = Rectangle(2, 4) 
print(r)
r.area()
print(r.area())
r.perimeter()
print(r.perimeter())





#super => parent class ko call krna  yani rectangle ko 
#idhr constructor override huwa hai 
# function  call k darmayan self nhi likhty  kuky self interpreter khud dlta hai.. 

#=====================================
#inherit hui vi class  ha ye 
# class Square(Rectangle):
#      def __init__(self, length): # constructor bnaya jo ik  hi length lega
#          super() .__init__(length, length)

# def __str__(self):
#     return "Square: " + super().__str__()

# square = Square (4)
# print(square.area())      
# print(square.perimeter()) 
#=====================================

# Constructor overloading ka matlab hai ke ek hi class ke andar tum multiple constructors bana sakti ho, lekin unka parameters alag-alag hote hain.


#Square asal me ek special rectangle hai jisme length = width hota hai.


# Yahan super().__init__(length, length) ka matlab hai ke parent class (Rectangle) ko dono values equal di ja rahi hain (kyunki square ke 4 sides barabar hote hain).



class Square(Rectangle):
     def __init__(self, length): 
         super() .__init__(length, length)

def __str__(self):
    return "Square: " + super().__str__()

square = Square (4)
print(square.area())      
print(square.perimeter()) 




#==============================================================================

























#___________________________[Polymorphism] 

class Students:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name} , Id: {self.id}"
    

s1 = Students("Hafsa" , "12")
s2 = Students("titi" , "10")

print(s1.__str__())

print(s2.__str__())

