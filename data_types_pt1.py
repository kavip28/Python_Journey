'''
Data Type       Class       Value
integers         int         1, 2, 3, 4, 5
floating point  float       1.0, 2.5, 3.14
booleans        bool        True, False
strings         str         "Hello", 'World'
list            list        [1, 2, 3], ['a', 'b', 'c']
dictionary     dict        {"name": "Alice", "age": 30}
tuple          tuple       (1, 2, 3), ('x', 'y', 'z')
set            set         {"cat", 99}
'''


# Numbers
import numbers


age = 23
print(age)
print("Age is type:", type(age))

#Floats
grade = 8.9
print(grade)
print("Grade is type:", type(grade))


#Booleans
is_student = True
print(is_student)
print("is_student is type:", type(is_student))

#Strings
name = "John"
print(name)
print("Name is type:", type(name))

#Lists
# Ordered sequence of elements
mixed = [1, 2, 3, 4, 5, True, "Hello", 3.14]
print(mixed)
print(mixed[7])  # Accessing the eighth element

#Dictionaries
student_grade = {"name": "Tom", "grade": 90}
print(student_grade)
print(student_grade["name"])  # Accessing the value associated with the "name" key


#Tuples
#Orderes sequence of elements, but immutable
coordinates = (10, 20)
print(coordinates)

#Sets
#Unordered
set = {1,2,"apple", "banana", "cherry"}
print(set)