# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_array(array):
    # Use a breakpoint in the code line below to debug your script.
    for item in array:
        print(item)  # Press Ctrl+F8 to toggle the breakpoint.

class MyClass:
  x = 5

class MyStudent:
  '''name = 'Oleksii'
  surname = 'Aleshchenko'
  age = 31
  eye_color = 'green-gray'
  hair_color = 'light' '''

  def __init__(self, name, surname, age, eye_color, hair_color):
      # Initialization for the Child class
      self.name = name
      self.surname = surname
      self.age = age
      self.eye_color = eye_color
      self.hair_color = hair_color
  def __str__(self):
      return 'name: ' + self.name + ",\tsurname: " + self.surname

  def __repr__(self):
      return '"name: ' + self.name + ", surname: " + self.surname + '"'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''print(MyClass.x)
print(MyStudent.name)
print(MyStudent.surname)
print(MyStudent.age)
print(MyStudent.eye_color)
print(MyStudent.hair_color)'''

MyStudent1 = MyStudent("Oleksii", "Aleshchenko", 31, "green-gray", 'light')
# MyStudent1.name = "Test"
print(MyStudent1.name)
MyStudent2 = MyStudent("Oleksii2", "Aleshchenko2", 31, "green-gray", 'light')
print(MyStudent2.name)

students = [MyStudent1, MyStudent2]
print(students)
print(MyStudent1)

students.sort(key=lambda x: x.name, reverse=True)
print("====Sorted array====")
print_array(students)

students.sort(key=lambda x: x.surname)
print("====Sorted array====")
print_array(students)