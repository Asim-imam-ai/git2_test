"""
PYTHON TUPLES - COMPREHENSIVE GUIDE
=====================================
Tuples are an immutable, ordered collection of elements in Python.
Once created, tuples cannot be modified (no adding, removing, or changing elements).
They are similar to lists but with the key difference of being immutable.
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================

# Method 1: Using parentheses with elements
fruits = ("apple", "banana", "orange", "mango")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True, None)

# Method 2: Without parentheses (still a tuple)
coordinates = 10, 20, 30
person = "Ali", 25, "Islamabad"

# Method 3: Using tuple() constructor
tuple_from_list = tuple([1, 2, 3, 4])
tuple_from_string = tuple("ABC")

# Method 4: Single element tuple (IMPORTANT: need trailing comma)
single = (42,)  # This is a tuple
single_wrong = (42)  # This is just an integer

# Method 5: Empty tuple
empty_tuple = ()
empty_tuple_2 = tuple()

print("Tuple Examples:")
print(f"fruits: {fruits}")
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"coordinates: {coordinates}")
print(f"single element tuple: {single}")
print(f"empty tuple: {empty_tuple}")
print(f"Type of single: {type(single)}, Type of single_wrong: {type(single_wrong)}")
print()

# ============================================================================
# 2. ACCESSING TUPLE ELEMENTS
# ============================================================================

# Using indexing (0-based)
first_fruit = fruits[0]
last_fruit = fruits[-1]
second_fruit = fruits[1]

print("Accessing elements:")
print(f"First fruit: {first_fruit}")
print(f"Last fruit: {last_fruit}")
print(f"Second fruit: {second_fruit}")
print()

# ============================================================================
# 3. SLICING TUPLES
# ============================================================================

# Slice syntax: tuple[start:end:step]
print("Slicing examples:")
print(f"First three fruits: {fruits[0:3]}")
print(f"From index 1 to end: {fruits[1:]}")
print(f"All except last: {fruits[:-1]}")
print(f"Every second element: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")
print()

# ============================================================================
# 4. TUPLE UNPACKING
# ============================================================================

# Unpack tuple elements into variables
x, y, z = coordinates
print(f"Unpacked coordinates - x: {x}, y: {y}, z: {z}")

# Unpack with assignment
a, b, *rest = numbers  # rest will be a list
print(f"a: {a}, b: {b}, rest: {rest}")

# Unpack person tuple
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")
print()

# ============================================================================
# 5. TUPLE METHODS
# ============================================================================

# Tuples have only two methods: count() and index()

sample_tuple = (1, 2, 3, 2, 4, 2, 5)

# count() - returns count of specified element
count_of_2 = sample_tuple.count(2)
print(f"Count of 2 in {sample_tuple}: {count_of_2}")

# index() - returns index of first occurrence
index_of_2 = sample_tuple.index(2)
print(f"Index of first 2: {index_of_2}")

# index() with range
try:
    index_of_2_after_first = sample_tuple.index(2, 2)  # Search from index 2
    print(f"Index of 2 starting from index 2: {index_of_2_after_first}")
except ValueError:
    print("Element not found")

# Trying to find non-existent element
try:
    sample_tuple.index(10)
except ValueError:
    print("ValueError: 10 is not in tuple")
print()

# ============================================================================
# 6. TUPLE LENGTH AND MEMBERSHIP
# ============================================================================

# len() - returns number of elements
print(f"Length of fruits: {len(fruits)}")

# in/not in - check if element exists
if "apple" in fruits:
    print("'apple' is in fruits tuple")

if "grape" not in fruits:
    print("'grape' is not in fruits tuple")
print()

# ============================================================================
# 7. ITERATING THROUGH TUPLES
# ============================================================================

print("Iterating through tuple:")
colors = ("red", "green", "blue", "yellow")

# Simple iteration
print("Colors:")
for color in colors:
    print(f"  {color}")

# Iteration with index
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")
print()

# ============================================================================
# 8. CONCATENATION AND REPETITION
# ============================================================================

# Concatenation (creates new tuple)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition (creates new tuple)
repeated = ("a", "b") * 3
print(f"Repetition: ('a', 'b') * 3 = {repeated}")
print()

# ============================================================================
# 9. NESTED TUPLES
# ============================================================================

# Tuples can contain other tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")
print(f"First inner tuple: {nested[0]}")
print(f"First element of first inner tuple: {nested[0][0]}")

# Mixed nested
matrix = ((1, 2, 3), ("a", "b", "c"), (True, False, None))
print(f"Matrix: {matrix}")
print(f"Element [1][2]: {matrix[1][2]}")
print()

# ============================================================================
# 10. IMMUTABILITY OF TUPLES
# ============================================================================

print("Demonstrating immutability:")

# Trying to modify element
try:
    numbers[0] = 10  # This will raise TypeError
except TypeError as e:
    print(f"Error: Cannot modify tuple - {e}")

# Trying to append
try:
    numbers.append(6)  # This will raise AttributeError
except AttributeError as e:
    print(f"Error: Cannot append to tuple - {e}")

# Trying to delete element
try:
    del numbers[0]  # This will raise TypeError
except TypeError as e:
    print(f"Error: Cannot delete from tuple - {e}")

print("Tuples are immutable - they cannot be changed after creation!")
print()

# ============================================================================
# 11. CONVERTING BETWEEN TUPLES AND LISTS
# ============================================================================

# List to Tuple
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print(f"List: {my_list}")
print(f"Converted to tuple: {my_tuple}")

# Tuple to List
my_tuple = (100, 200, 300)
my_list = list(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"Converted to list: {my_list}")
print()

# ============================================================================
# 12. TUPLE PACKING
# ============================================================================

# Packing: collecting values into a tuple
name = "Ahmed"
age = 25
city = "Karachi"
person_info = (name, age, city)  # Packing
print(f"Packed tuple: {person_info}")

# Unpacking (reverse of packing)
n, a, c = person_info  # Unpacking
print(f"Unpacked - Name: {n}, Age: {a}, City: {c}")
print()

# ============================================================================
# 13. TUPLE COMPARISON
# ============================================================================

# Tuples are compared lexicographically (like strings)
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)

print("Tuple comparison:")
print(f"{tuple_a} == {tuple_c}: {tuple_a == tuple_c}")
print(f"{tuple_a} < {tuple_b}: {tuple_a < tuple_b}")
print(f"{tuple_b} > {tuple_a}: {tuple_b > tuple_a}")
print()

# ============================================================================
# 14. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Function returning multiple values
def get_user_info():
    return ("Ali", 25, "ali@example.com")

user = get_user_info()
print(f"User info: {user}")
username, user_age, email = get_user_info()
print(f"Username: {username}, Age: {user_age}, Email: {email}")

# Example 2: Using tuple as dictionary key (lists can't be used)
coordinates_dict = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (5, 10): "point_A"
}
print(f"\nCoordinates mapping: {coordinates_dict}")
print(f"Value at (0, 0): {coordinates_dict[(0, 0)]}")

# Example 3: Tuple in sorting (sorts by first element, then second, etc.)
students = [
    ("Ali", 85),
    ("Sara", 90),
    ("Ahmed", 85),
    ("Fatima", 88)
]
print(f"\nOriginal: {students}")
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
print(f"Sorted by score then name: {sorted_students}")

# Example 4: Using named tuples
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print(f"\nNamed tuple: {p}")
print(f"Access by attribute: x={p.x}, y={p.y}, z={p.z}")
print()

# ============================================================================
# 15. DIFFERENCES BETWEEN TUPLES AND LISTS
# ============================================================================

print("""
TUPLES vs LISTS:
================
TUPLES:
  - Immutable (cannot change after creation)
  - Created with ()
  - Slightly faster than lists
  - Can be used as dictionary keys
  - Only have count() and index() methods
  - Memory efficient
  - Better for protecting data

LISTS:
  - Mutable (can be changed)
  - Created with []
  - More flexible and versatile
  - Cannot be used as dictionary keys
  - Have many methods (append, remove, sort, etc.)
  - Use more memory
  - Better for data manipulation

WHEN TO USE TUPLES:
  - When data should not be modified
  - As dictionary keys
  - For function return values (multiple values)
  - To protect data from accidental changes
  - For slightly better performance
""")

# ============================================================================
# 16. TUPLE OPERATIONS SUMMARY
# ============================================================================

print("""
TUPLE OPERATIONS SUMMARY:
=========================
Indexing:       tuple[index]
Slicing:        tuple[start:end:step]
Length:         len(tuple)
Concatenation:  tuple1 + tuple2
Repetition:     tuple * n
Membership:     element in tuple
Iteration:      for item in tuple:
Unpacking:      a, b, c = tuple
Count:          tuple.count(element)
Index:          tuple.index(element)
Conversion:     tuple(iterable)
""")
