class Person:
   def __init__(self, name, age):
    self.name = name
    self.age =age

   def greet(self):
      print(f"Hello, my name is {self.name} and am {self.age} years old ")


person1  = Person("Abdi", 20)
print(person1.greet())


class Student(Person):
  def __init__(self,name,age,student_id):
    super().__init__(name,age) 
    self.student_id = student_id

  def study(self):
    print(f"my nmae is {self.name}")




student1 = Student("Alice",23, 34)
print(student1.name)