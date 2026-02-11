'''
class Friend:

      say = 'Hello'              # Class attribute

      def __init__ (self, name, type_of, gender):      #state = attribute

            self.name = name                          #instance attribute
            self.type_of = type_of                  #instance attribute
            self.gender = gender                   #instance attribute

      def conversation (self,talk):                                     # behaviour = method
            
            self.talk = talk
            return 

      def __str__ (self):                                   #string

            return f"{Friend.say}! {self.name} and I are {self.type_of}s. Her gender is {self.gender}"

friend1 = Friend("Aleena", "Just friend", "girl")               #identity = object
friend2 = Friend("Alvina", "friend", "girl")

print(friend1)   
print(friend2)

#updated classs and instance attribute

Friend.say = "Assalam o alikum"
friend2.name = 'Ali'
friend2.type_of = "friend"
friend2.gender = "boy"                              
print(f"{Friend.say}! {friend2.name} and I are {friend2.type_of}s. His gender is {friend2.gender}")

class Cat:                                #class 

      family = 'Mammel'                #class attribute
      animal_type = 'cat'                #class attribute

      def sound (self):                     #method = behaviour

            print("The animal belongs to the family: ", self.family)      
            print("The animal is a: ", self.animal_type)
            
      def food (self):                     #method

            print('The cat eats meat')

Zoge = Cat()                                

print(Zoge.family)
print(Zoge.animal_type)

Zoge.sound()
Zoge.food()

class Animal:

      sound1 = "Meaw!"
      sound2 = "Woof!"

      def __init__ (self, name):

            self.name = name

      def sound(self):

            print('Error')

class Cat(Animal):

      def sound(self):

             return Animal.sound1

zoge = Cat("zoge")
print(f'The name of cat is {zoge.name}, and it says {zoge.sound()}')

class Shape:

      Type_of = "basic"

      def __init__ (self, color):

            self.color = color

      def size(self):

            raise NotImplementedError("This method must be in subclass.")

class Circle(Shape):

      def __init__ (self, color, radius):
            super().__init__ (color)

            self.radius = radius

      def area (self):

            return 3.14 * self.radius ** 2
      
circle0=Shape("Red")
circle1 = Circle("Blue", 5)

print(circle1.area())


class Person:
    
    def display(self):
      
        return f"The salary of Vimsa is $ 2500. And she is 25 years old"

class Employee(Person):

    def display(self):

        return "Hey there!"

vimsa = [Employee(), Person()]
for vimsas in vimsa:
      print(vimsas.display())

#overriding
#polymorphism

class Calculator:

      def __init__ (self, value, method):

            self.value = value
            self.method = method

      def addition(self):

            return self.value + self.method            

      def subtraction(self):

            return self.value - self.method            

      def multiplication(self):

            return self.value * self.method            

      def division(self):

            return self.value / self.method            

      def power(self):

            return self.value * self.method            

value_1 = Calculator(2, 3)
print(value_1.division())
value_2 = Calculator(value_1.value, 3)
print(value_2.addition())

class Family:

      def __init__ (self, parents, children):

            self.parents = parents
            self.children = children

      mother = "Hey! I am mother of Musfira. My good name is Samina. Nice to meet you."

      father  = "Hello! I am father of Musfira. My good name is Ateeq. Good to see you here."

      brother = "Aoa! I am brother of Musfira. My good name is Ahmed. Glad to meet with you"

      elder_sister = "Hey! I am elder sister of Musfira. My good name is Inbisat. Nice to meet you"

      younger_sister = "Hey! I am younger sister of Musfira. My good name is Vimsa. Nice to meet you"

print('1. mother')
print('2. father')
print('3. brother')
print('4. elder sister')
print('5. younger sister')
print('6. someone else')
name = str(input("Enter your relationship with Musfira: "))
if name == '1':
      
      print(Family.mother)
elif name == "4":
      
      print(Family.elder_sister)
elif name == "5":
      
      print(Family.younger_sister)
elif name == "3":
      
      print(Family.brother)
elif name == "2":
      
      print(Family.father)
else:

      new_name = str(input("Enter your name here: "))
      new_relationship = str(input("Enter your relationship here: "))
      
      print(f"Hello! This is {new_name}. Musfira and I are {new_relationship}. Nice to meet you.")

fr = [1, 2, 3, 4, 5, 6]
gr = [2, 4, 6, 8, 10]

x =filter(lambda fr: (fr, gr), fr) 
x =map(lambda gr: (fr, gr), gr) 
print(min(fr))
print(max(gr))

class Creatures:

      _name = 'Tony'

      def __init__ (self, hands, feets):

            self.hands = hands
            self.feets = feets

      def display(self):

            return f"The {Creatures._name} has {self.hands} hands, and {self.feets} feets. Hope this info helps you!"

class Human(Creatures):

      def __init__ (self, hands, feets, brain):
            super().__init__(hands, feets)

            self.brain = brain

      def thinking(self):

            return f"The {Creatures._name} has {self.hands} hands, {self.feets} feets, and {self.brain} capacity to think."

      def meal(self):

            return f"The creature eats food and works hard to reach it's destination."

class Cat(Creatures):

      def __init__ (self, hands, feets, tail):
            super().__init__(hands, feets)

            self.tail = tail

      def display(self):

            return f"The {Creatures._name} has {self.hands} hands, {self.feets} feets, and {self.tail} tails."

      def meal(self):

            return f"The creature eats food"

human_1 = Human(2, 2, '100%')
print(human_1.thinking())
print(human_1.meal())
cat_1 = Cat(0, 4, 1)
print(cat_1.display())
print(cat_1.meal())
print(dir(Creatures))

class Human:

      name = "Vimsa"
      age = 11
      Class = 6
      
      def __init__ (self, hands, feets, body):

            self.hands = hands
            self.feets = feets
            self.body = body

      def display(self):

            return f"Assalamoalikum! This is {Human.name}. My age is {Human.age}, and I am {Human.Class} grade."

      def add_dis(self):

            return f"I have {self.hands} hands. and {self.feets} feets. My body posture is {self.body}."

class Activities(Human):

      def __init__  (self, hands, feets, body, meals, play, study):
            super().__init__ (hands, feets, body)

            self.meals = meals
            self.play = play
            self.study = study

      def meal(self):

            return f"My favourate food is {self.meals}"

      def playing(self):

            return f"I plays {self.play}."

      def studing(self):

            return f"My study time is {self.study}."

      def conclusion(self):

            return "As a result, I am an intelligent human. I don't know why I am still here... Do you know?"

human_1 = Activities(2, 2, "in a good condition", "fast food and desi food, including healty food like fruits, vegies, etc...", "IPad, TV, Talking, Joking, etc", "4 to 5 hours")
print(human_1.display())
print(human_1.add_dis())
print(human_1.meal())
print(human_1.playing())
print(human_1.studing())
print(human_1.conclusion())
#private member
class Car:

      __name = None
      __year_of_invention = None

      def __init__ (self, name, year_of_invention, condition, color):

            self.__name = name
            self.__year_of_invention = year_of_invention
            self.__condition = condition
            self.__color = color

      def __display(self):

            print("Name: ", self.__name)
            print("Year of invention: ", self.__year_of_invention)
            print("Condition: ", self.__condition)
            print("Color: ", self.__color)
            
      def details(self):

            self.__display()
            
car_1 = Car("Honda", 2003, "good", "white")
car_2 = Car("Civic", 2004, "good", "black")
print(car_1._Car__name)
print(car_1._Car__year_of_invention)
print(car_2._Car__condition)
print(car_2._Car__color)
print(dir(Car))
car_1.details()
car_2.details()

#protected, private, and public members, inheretence, Encapsulation, class, attributes, method,  lambda, class/method instance, base/derive class

class Human:
    name = None  # public
    __roll_number = None  # private
    _department = None  # protected

    def __init__(self, name, roll_num, dep):
        self.name = name
        self.__roll_number = roll_num
        self._department = dep

    def display(self):
        print("Name: ", self.name)

    def __student_roll_number(self):
        print("Roll number: ", self.__roll_number)

    def _student_dep(self):
        print("Department: ", self._department)

    def display_access_details(self):
        self.__student_roll_number()

class Departments(Human):
    def __init__(self, name, roll_num, dep):
        super().__init__(name, roll_num, dep)

    def access_departmental_details(self):
        self._student_dep()

Stud_1 = Departments("Ali", 271143657, "Computer Science")

Stud_1.display_access_details()
Stud_1.access_departmental_details()
Stud_1._student_dep()
Stud_1._Human__student_roll_number()
Stud_1.display()
print()
print("Accessing departmental details: ", Stud_1.access_departmental_details())
print("Displaying details: ", Stud_1.display_access_details())

#polymorphism
a = [0, 2, 5, 8]
print (max(a))
print (len(a))
a = ["a","z","zz"]
print(len(a))
print(max(a))

def add(a, b):

      return a + b
def subtract(a, b):

      return a * b

print(add(12, 56))
print(add("Musfira", "Sehar"))
print(subtract(12, 56))
c = subtract("Musfira", 2)
print(len(c))
print(max(c))
print([1, 2]+[3, 4])
'''

j = ['a', 'b', 'c']
i = j
if i is j:
      print(max(i))
else:
      print("Error")

























