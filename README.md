# json-python-quiz

├── New folder
├── console based quiz
├── README.md
├── performance.json
├── P2 Project.py (1800 tokens)
└── ramdom class...attribues.py (2700 tokens)


/New folder:
--------------------------------------------------------------------------------
1 | 


--------------------------------------------------------------------------------
/console based quiz:
--------------------------------------------------------------------------------
1 | 


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
1 | # json-python-quiz


--------------------------------------------------------------------------------
/performance.json:
--------------------------------------------------------------------------------
1 | {
2 |     "maths": {
3 |         "low": {
4 |             "Ali": 4
5 |         }
6 |     }
7 | }


--------------------------------------------------------------------------------
/P2 Project.py:
--------------------------------------------------------------------------------
  1 | import json
  2 | import random
  3 | import os
  4 | 
  5 | # Utility Functions
  6 | def load_data(file_name, default_data=None):
  7 |     """Load data from a JSON file, creating the file with default data if it doesn't exist."""
  8 |     if not os.path.exists(file_name):
  9 |         if default_data is not None:
 10 |             save_data(file_name, default_data)
 11 |         return default_data or {}
 12 |     with open(file_name, 'r') as file:
 13 |         return json.load(file)
 14 | 
 15 | def save_data(file_name, data):
 16 |     """Save data to a JSON file."""
 17 |     with open(file_name, 'w') as file:
 18 |         json.dump(data, file, indent=4)
 19 | 
 20 | def initialize_questions():
 21 |     """Initialize default questions for all subjects and difficulties."""
 22 |     return {
 23 |         "maths": {
 24 |             "low": [
 25 |                 {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4", "hint": "First even number."},
 26 |                 {"question": "5 x 1 = ?", "options": ["1", "5", "10", "15"], "answer": "5", "hint": "Anything multiplied by 1 is itself."},
 27 |                 {"question": "10 - 3 = ?", "options": ["6", "7", "8", "9"], "answer": "7", "hint": "Count backward."},
 28 |                 {"question": "12 / 4 = ?", "options": ["2", "3", "4", "6"], "answer": "3", "hint": "Divide 12 into 4 equal parts."},
 29 |                 {"question": "3 x 3 = ?", "options": ["6", "7", "8", "9"], "answer": "9", "hint": "Square of 3."}
 30 |             ]
 31 |         }
 32 |     }
 33 | 
 34 | # Student Class
 35 | class Student:
 36 |     def __init__(self, username, password, points=0):
 37 |         self.username = username
 38 |         self.password = password
 39 |         self.points = points
 40 | 
 41 |     def attempt_quiz(self, questions):
 42 |         """Allow the student to attempt a quiz with next/submit options."""
 43 |         score = 0
 44 |         total_questions = len(questions)
 45 |         question_index = 0
 46 | 
 47 |         while question_index < total_questions:
 48 |             q = questions[question_index]
 49 |             print(f"\nQuestion {question_index + 1}: {q['question']}")
 50 |             print("Options:")
 51 |             for i, option in enumerate(q['options'], start=1):
 52 |                 print(f"{i}. {option}")
 53 |             answer = input("Enter the number of your choice: ").strip()
 54 | 
 55 |             try:
 56 |                 if q['options'][int(answer) - 1] == q['answer']:
 57 |                     print("Correct!")
 58 |                     score += 1
 59 |                 else:
 60 |                     print(f"Incorrect! Hint: {q['hint']}")
 61 |             except (ValueError, IndexError):
 62 |                 print("Invalid input. Moving to the next question.")
 63 |             
 64 |             if question_index < total_questions - 1:
 65 |                 choice = input("Enter 'N' for Next Question or 'S' to Submit: ").strip().upper()
 66 |                 if choice == 'S':
 67 |                     break
 68 |             question_index += 1
 69 | 
 70 |         print(f"\nQuiz Submitted! Your score: {score}/{total_questions}")
 71 |         return score
 72 | 
 73 | # Instructor Class
 74 | class Instructor:
 75 |     def __init__(self, username, password):
 76 |         self.username = username
 77 |         self.password = password
 78 | 
 79 | # Quiz System
 80 | class QuizSystem:
 81 |     def __init__(self):
 82 |         self.users = load_data("users.json", {})
 83 |         self.questions = load_data("questions.json", initialize_questions())
 84 |         self.performance = load_data("performance.json", {})
 85 | 
 86 |     def save_state(self):
 87 |         save_data("users.json", self.users)
 88 |         save_data("questions.json", self.questions)
 89 |         save_data("performance.json", self.performance)
 90 | 
 91 |     def register_user(self, role):
 92 |         username = input("Enter a username: ").strip()
 93 |         password = input("Enter a password: ").strip()
 94 |         if username in self.users:
 95 |             print("Username already exists!")
 96 |         else:
 97 |             self.users[username] = {"password": password, "role": role, "points": 0}
 98 |             print("User registered successfully!")
 99 |             self.save_state()
100 | 
101 |     def login_user(self):
102 |         username = input("Enter your username: ").strip()
103 |         password = input("Enter your password: ").strip()
104 |         if username in self.users and self.users[username]["password"] == password:
105 |             print("Login successful!")
106 |             return username
107 |         else:
108 |             print("Invalid username or password.")
109 |             return None
110 | 
111 |     def run(self):
112 |         print("=== Welcome to the Quiz System! ===")
113 |         while True:
114 |             action = input("Choose an action: R (Register), L (Login), E (Exit): ").strip().upper()
115 |             if action == "R":
116 |                 role = input("Register as S (Student) or I (Instructor): ").strip().upper()
117 |                 if role == "S":
118 |                     self.register_user("student")
119 |                 elif role == "I":
120 |                     self.register_user("instructor")
121 |                 else:
122 |                     print("Invalid role.")
123 |             elif action == "L":
124 |                 username = self.login_user()
125 |                 if username:
126 |                     role = self.users[username]["role"]
127 |                     if role == "student":
128 |                         self.student_menu(username)
129 |                     elif role == "instructor":
130 |                         self.instructor_menu(username)
131 |             elif action == "E":
132 |                 print("Goodbye!")
133 |                 break
134 |             else:
135 |                 print("Invalid action.")
136 | 
137 |     def student_menu(self, username):
138 |         student = Student(username, self.users[username]["password"], self.users[username]["points"])
139 |         while True:
140 |             print("\n--- Student Menu ---")
141 |             choice = input("Choose an action: Q (Attempt Quiz), V (View Results), L (Logout): ").strip().upper()
142 |             if choice == "Q":
143 |                 subject = input("Enter subject (maths): ").strip().lower()
144 |                 difficulty = "low"  # Default difficulty for now
145 |                 if subject in self.questions:
146 |                     questions = random.sample(self.questions[subject][difficulty], min(5, len(self.questions[subject][difficulty])))
147 |                     score = student.attempt_quiz(questions)
148 |                     self.performance.setdefault(subject, {}).setdefault(difficulty, {}).setdefault(username, score)
149 |                     self.save_state()
150 |                 else:
151 |                     print("Invalid subject.")
152 |             elif choice == "V":
153 |                 print(f"\n--- Results for {username} ---")
154 |                 for subject, levels in self.performance.items():
155 |                     for level, scores in levels.items():
156 |                         if username in scores:
157 |                             print(f"Subject: {subject}, Difficulty: {level}, Score: {scores[username]}")
158 |             elif choice == "L":
159 |                 break
160 |             else:
161 |                 print("Invalid choice.")
162 | 
163 |     def instructor_menu(self, username):
164 |         instructor = Instructor(username, self.users[username]["password"])
165 |         while True:
166 |             print("\n--- Instructor Menu ---")
167 |             choice = input("Choose an action: V (View Performance), L (Logout): ").strip().upper()
168 |             if choice == "V":
169 |                 subject = input("Enter subject to view performance: ").strip().lower()
170 |                 subject_data = self.performance.get(subject, {})
171 |                 if not subject_data:
172 |                     print("No performance data available for this subject.")
173 |                     continue
174 |                 for level, scores in subject_data.items():
175 |                     print(f"Difficulty: {level}")
176 |                     for student, score in scores.items():
177 |                         print(f"{student}: {score}")
178 |             elif choice == "L":
179 |                 break
180 |             else:
181 |                 print("Invalid choice.")
182 | 
183 | # Run the Quiz System
184 | quiz_system = QuizSystem()
185 | quiz_system.run()
186 | 


--------------------------------------------------------------------------------
/ramdom class...attribues.py:
--------------------------------------------------------------------------------
  1 | '''
  2 | class Friend:
  3 | 
  4 |       say = 'Hello'              # Class attribute
  5 | 
  6 |       def __init__ (self, name, type_of, gender):      #state = attribute
  7 | 
  8 |             self.name = name                          #instance attribute
  9 |             self.type_of = type_of                  #instance attribute
 10 |             self.gender = gender                   #instance attribute
 11 | 
 12 |       def conversation (self,talk):                                     # behaviour = method
 13 |             
 14 |             self.talk = talk
 15 |             return 
 16 | 
 17 |       def __str__ (self):                                   #string
 18 | 
 19 |             return f"{Friend.say}! {self.name} and I are {self.type_of}s. Her gender is {self.gender}"
 20 | 
 21 | friend1 = Friend("Aleena", "Just friend", "girl")               #identity = object
 22 | friend2 = Friend("Alvina", "friend", "girl")
 23 | 
 24 | print(friend1)   
 25 | print(friend2)
 26 | 
 27 | #updated classs and instance attribute
 28 | 
 29 | Friend.say = "Assalam o alikum"
 30 | friend2.name = 'Ali'
 31 | friend2.type_of = "friend"
 32 | friend2.gender = "boy"                              
 33 | print(f"{Friend.say}! {friend2.name} and I are {friend2.type_of}s. His gender is {friend2.gender}")
 34 | 
 35 | class Cat:                                #class 
 36 | 
 37 |       family = 'Mammel'                #class attribute
 38 |       animal_type = 'cat'                #class attribute
 39 | 
 40 |       def sound (self):                     #method = behaviour
 41 | 
 42 |             print("The animal belongs to the family: ", self.family)      
 43 |             print("The animal is a: ", self.animal_type)
 44 |             
 45 |       def food (self):                     #method
 46 | 
 47 |             print('The cat eats meat')
 48 | 
 49 | Zoge = Cat()                                
 50 | 
 51 | print(Zoge.family)
 52 | print(Zoge.animal_type)
 53 | 
 54 | Zoge.sound()
 55 | Zoge.food()
 56 | 
 57 | class Animal:
 58 | 
 59 |       sound1 = "Meaw!"
 60 |       sound2 = "Woof!"
 61 | 
 62 |       def __init__ (self, name):
 63 | 
 64 |             self.name = name
 65 | 
 66 |       def sound(self):
 67 | 
 68 |             print('Error')
 69 | 
 70 | class Cat(Animal):
 71 | 
 72 |       def sound(self):
 73 | 
 74 |              return Animal.sound1
 75 | 
 76 | zoge = Cat("zoge")
 77 | print(f'The name of cat is {zoge.name}, and it says {zoge.sound()}')
 78 | 
 79 | class Shape:
 80 | 
 81 |       Type_of = "basic"
 82 | 
 83 |       def __init__ (self, color):
 84 | 
 85 |             self.color = color
 86 | 
 87 |       def size(self):
 88 | 
 89 |             raise NotImplementedError("This method must be in subclass.")
 90 | 
 91 | class Circle(Shape):
 92 | 
 93 |       def __init__ (self, color, radius):
 94 |             super().__init__ (color)
 95 | 
 96 |             self.radius = radius
 97 | 
 98 |       def area (self):
 99 | 
100 |             return 3.14 * self.radius ** 2
101 |       
102 | circle0=Shape("Red")
103 | circle1 = Circle("Blue", 5)
104 | 
105 | print(circle1.area())
106 | 
107 | 
108 | class Person:
109 |     
110 |     def display(self):
111 |       
112 |         return f"The salary of Vimsa is $ 2500. And she is 25 years old"
113 | 
114 | class Employee(Person):
115 | 
116 |     def display(self):
117 | 
118 |         return "Hey there!"
119 | 
120 | vimsa = [Employee(), Person()]
121 | for vimsas in vimsa:
122 |       print(vimsas.display())
123 | 
124 | #overriding
125 | #polymorphism
126 | 
127 | class Calculator:
128 | 
129 |       def __init__ (self, value, method):
130 | 
131 |             self.value = value
132 |             self.method = method
133 | 
134 |       def addition(self):
135 | 
136 |             return self.value + self.method            
137 | 
138 |       def subtraction(self):
139 | 
140 |             return self.value - self.method            
141 | 
142 |       def multiplication(self):
143 | 
144 |             return self.value * self.method            
145 | 
146 |       def division(self):
147 | 
148 |             return self.value / self.method            
149 | 
150 |       def power(self):
151 | 
152 |             return self.value * self.method            
153 | 
154 | value_1 = Calculator(2, 3)
155 | print(value_1.division())
156 | value_2 = Calculator(value_1.value, 3)
157 | print(value_2.addition())
158 | 
159 | class Family:
160 | 
161 |       def __init__ (self, parents, children):
162 | 
163 |             self.parents = parents
164 |             self.children = children
165 | 
166 |       mother = "Hey! I am mother of Musfira. My good name is Samina. Nice to meet you."
167 | 
168 |       father  = "Hello! I am father of Musfira. My good name is Ateeq. Good to see you here."
169 | 
170 |       brother = "Aoa! I am brother of Musfira. My good name is Ahmed. Glad to meet with you"
171 | 
172 |       elder_sister = "Hey! I am elder sister of Musfira. My good name is Inbisat. Nice to meet you"
173 | 
174 |       younger_sister = "Hey! I am younger sister of Musfira. My good name is Vimsa. Nice to meet you"
175 | 
176 | print('1. mother')
177 | print('2. father')
178 | print('3. brother')
179 | print('4. elder sister')
180 | print('5. younger sister')
181 | print('6. someone else')
182 | name = str(input("Enter your relationship with Musfira: "))
183 | if name == '1':
184 |       
185 |       print(Family.mother)
186 | elif name == "4":
187 |       
188 |       print(Family.elder_sister)
189 | elif name == "5":
190 |       
191 |       print(Family.younger_sister)
192 | elif name == "3":
193 |       
194 |       print(Family.brother)
195 | elif name == "2":
196 |       
197 |       print(Family.father)
198 | else:
199 | 
200 |       new_name = str(input("Enter your name here: "))
201 |       new_relationship = str(input("Enter your relationship here: "))
202 |       
203 |       print(f"Hello! This is {new_name}. Musfira and I are {new_relationship}. Nice to meet you.")
204 | 
205 | fr = [1, 2, 3, 4, 5, 6]
206 | gr = [2, 4, 6, 8, 10]
207 | 
208 | x =filter(lambda fr: (fr, gr), fr) 
209 | x =map(lambda gr: (fr, gr), gr) 
210 | print(min(fr))
211 | print(max(gr))
212 | 
213 | class Creatures:
214 | 
215 |       _name = 'Tony'
216 | 
217 |       def __init__ (self, hands, feets):
218 | 
219 |             self.hands = hands
220 |             self.feets = feets
221 | 
222 |       def display(self):
223 | 
224 |             return f"The {Creatures._name} has {self.hands} hands, and {self.feets} feets. Hope this info helps you!"
225 | 
226 | class Human(Creatures):
227 | 
228 |       def __init__ (self, hands, feets, brain):
229 |             super().__init__(hands, feets)
230 | 
231 |             self.brain = brain
232 | 
233 |       def thinking(self):
234 | 
235 |             return f"The {Creatures._name} has {self.hands} hands, {self.feets} feets, and {self.brain} capacity to think."
236 | 
237 |       def meal(self):
238 | 
239 |             return f"The creature eats food and works hard to reach it's destination."
240 | 
241 | class Cat(Creatures):
242 | 
243 |       def __init__ (self, hands, feets, tail):
244 |             super().__init__(hands, feets)
245 | 
246 |             self.tail = tail
247 | 
248 |       def display(self):
249 | 
250 |             return f"The {Creatures._name} has {self.hands} hands, {self.feets} feets, and {self.tail} tails."
251 | 
252 |       def meal(self):
253 | 
254 |             return f"The creature eats food"
255 | 
256 | human_1 = Human(2, 2, '100%')
257 | print(human_1.thinking())
258 | print(human_1.meal())
259 | cat_1 = Cat(0, 4, 1)
260 | print(cat_1.display())
261 | print(cat_1.meal())
262 | print(dir(Creatures))
263 | 
264 | class Human:
265 | 
266 |       name = "Vimsa"
267 |       age = 11
268 |       Class = 6
269 |       
270 |       def __init__ (self, hands, feets, body):
271 | 
272 |             self.hands = hands
273 |             self.feets = feets
274 |             self.body = body
275 | 
276 |       def display(self):
277 | 
278 |             return f"Assalamoalikum! This is {Human.name}. My age is {Human.age}, and I am {Human.Class} grade."
279 | 
280 |       def add_dis(self):
281 | 
282 |             return f"I have {self.hands} hands. and {self.feets} feets. My body posture is {self.body}."
283 | 
284 | class Activities(Human):
285 | 
286 |       def __init__  (self, hands, feets, body, meals, play, study):
287 |             super().__init__ (hands, feets, body)
288 | 
289 |             self.meals = meals
290 |             self.play = play
291 |             self.study = study
292 | 
293 |       def meal(self):
294 | 
295 |             return f"My favourate food is {self.meals}"
296 | 
297 |       def playing(self):
298 | 
299 |             return f"I plays {self.play}."
300 | 
301 |       def studing(self):
302 | 
303 |             return f"My study time is {self.study}."
304 | 
305 |       def conclusion(self):
306 | 
307 |             return "As a result, I am an intelligent human. I don't know why I am still here... Do you know?"
308 | 
309 | human_1 = Activities(2, 2, "in a good condition", "fast food and desi food, including healty food like fruits, vegies, etc...", "IPad, TV, Talking, Joking, etc", "4 to 5 hours")
310 | print(human_1.display())
311 | print(human_1.add_dis())
312 | print(human_1.meal())
313 | print(human_1.playing())
314 | print(human_1.studing())
315 | print(human_1.conclusion())
316 | #private member
317 | class Car:
318 | 
319 |       __name = None
320 |       __year_of_invention = None
321 | 
322 |       def __init__ (self, name, year_of_invention, condition, color):
323 | 
324 |             self.__name = name
325 |             self.__year_of_invention = year_of_invention
326 |             self.__condition = condition
327 |             self.__color = color
328 | 
329 |       def __display(self):
330 | 
331 |             print("Name: ", self.__name)
332 |             print("Year of invention: ", self.__year_of_invention)
333 |             print("Condition: ", self.__condition)
334 |             print("Color: ", self.__color)
335 |             
336 |       def details(self):
337 | 
338 |             self.__display()
339 |             
340 | car_1 = Car("Honda", 2003, "good", "white")
341 | car_2 = Car("Civic", 2004, "good", "black")
342 | print(car_1._Car__name)
343 | print(car_1._Car__year_of_invention)
344 | print(car_2._Car__condition)
345 | print(car_2._Car__color)
346 | print(dir(Car))
347 | car_1.details()
348 | car_2.details()
349 | 
350 | #protected, private, and public members, inheretence, Encapsulation, class, attributes, method,  lambda, class/method instance, base/derive class
351 | 
352 | class Human:
353 |     name = None  # public
354 |     __roll_number = None  # private
355 |     _department = None  # protected
356 | 
357 |     def __init__(self, name, roll_num, dep):
358 |         self.name = name
359 |         self.__roll_number = roll_num
360 |         self._department = dep
361 | 
362 |     def display(self):
363 |         print("Name: ", self.name)
364 | 
365 |     def __student_roll_number(self):
366 |         print("Roll number: ", self.__roll_number)
367 | 
368 |     def _student_dep(self):
369 |         print("Department: ", self._department)
370 | 
371 |     def display_access_details(self):
372 |         self.__student_roll_number()
373 | 
374 | class Departments(Human):
375 |     def __init__(self, name, roll_num, dep):
376 |         super().__init__(name, roll_num, dep)
377 | 
378 |     def access_departmental_details(self):
379 |         self._student_dep()
380 | 
381 | Stud_1 = Departments("Ali", 271143657, "Computer Science")
382 | 
383 | Stud_1.display_access_details()
384 | Stud_1.access_departmental_details()
385 | Stud_1._student_dep()
386 | Stud_1._Human__student_roll_number()
387 | Stud_1.display()
388 | print()
389 | print("Accessing departmental details: ", Stud_1.access_departmental_details())
390 | print("Displaying details: ", Stud_1.display_access_details())
391 | 
392 | #polymorphism
393 | a = [0, 2, 5, 8]
394 | print (max(a))
395 | print (len(a))
396 | a = ["a","z","zz"]
397 | print(len(a))
398 | print(max(a))
399 | 
400 | def add(a, b):
401 | 
402 |       return a + b
403 | def subtract(a, b):
404 | 
405 |       return a * b
406 | 
407 | print(add(12, 56))
408 | print(add("Musfira", "Sehar"))
409 | print(subtract(12, 56))
410 | c = subtract("Musfira", 2)
411 | print(len(c))
412 | print(max(c))
413 | print([1, 2]+[3, 4])
414 | '''
415 | 
416 | j = ['a', 'b', 'c']
417 | i = j
418 | if i is j:
419 |       print(max(i))
420 | else:
421 |       print("Error")

--------------------------------------------------------------------------------
