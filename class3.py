"""
PYTHON DICTIONARIES - COMPREHENSIVE GUIDE
==========================================
Dictionaries are one of Python's most important data structures.
They store data in key-value pairs and are mutable, unordered (in Python < 3.7) 
or ordered (in Python 3.7+) collections.
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================

# Method 1: Using curly braces with key-value pairs
student = {"name": "Ali", "age": 20, "gpa": 3.8}

# Method 2: Using dict() constructor
person = dict(name="Sara", age=25, city="Karachi")

# Method 3: Empty dictionary
empty_dict = {}
empty_dict_2 = dict()

# Method 4: Using dict() with list of tuples
scores = dict([("math", 95), ("english", 88), ("science", 92)])

print("Dictionary Examples:")
print(f"student: {student}")
print(f"person: {person}")
print()

# ============================================================================
# 2. ACCESSING DICTIONARY VALUES
# ============================================================================

# Using square brackets (raises KeyError if key doesn't exist)
name = student["name"]
print(f"Student name: {name}")

# Using .get() method (returns None or default value if key doesn't exist)
age = student.get("age")
gpa = student.get("gpa", 0)
unknown = student.get("email", "Not found")
print(f"Age: {age}, GPA: {gpa}, Email: {unknown}")
print()

# ============================================================================
# 3. ADDING AND MODIFYING VALUES
# ============================================================================

# Add new key-value pair
student["email"] = "ali@example.com"
student["grade"] = "A"

# Modify existing value
student["age"] = 21

# Update multiple values at once
student.update({"city": "Islamabad", "phone": "03001234567"})

print("After modifications:")
print(f"student: {student}")
print()

# ============================================================================
# 4. DELETING ITEMS
# ============================================================================

# Delete specific key using del
del student["phone"]

# Remove and return value using pop()
email = student.pop("email")
print(f"Removed email: {email}")

# Remove and return last item using popitem()
last_item = student.popitem()
print(f"Removed item: {last_item}")

# Clear all items
test_dict = {"a": 1, "b": 2}
test_dict.clear()
print(f"Cleared dictionary: {test_dict}")
print()

# ============================================================================
# 5. DICTIONARY METHODS
# ============================================================================

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "white"}

# .keys() - returns all keys
print(f"Keys: {car.keys()}")

# .values() - returns all values
print(f"Values: {car.values()}")

# .items() - returns key-value pairs as tuples
print(f"Items: {car.items()}")

# .copy() - creates a shallow copy
car_copy = car.copy()

# .setdefault() - returns value if exists, otherwise adds key with default value
print(f"Price: {car.setdefault('price', 50000)}")
print(f"After setdefault: {car}")
print()

# ============================================================================
# 6. ITERATING THROUGH DICTIONARIES
# ============================================================================

print("Iterating through dictionary:")
book = {"title": "Python Basics", "author": "John Doe", "pages": 350}

# Iterate through keys
print("Keys:")
for key in book:
    print(f"  {key}")

# Iterate through values
print("Values:")
for value in book.values():
    print(f"  {value}")

# Iterate through key-value pairs
print("Key-Value pairs:")
for key, value in book.items():
    print(f"  {key}: {value}")
print()

# ============================================================================
# 7. CHECKING MEMBERSHIP
# ============================================================================

# Check if key exists
if "title" in book:
    print("'title' key exists in book dictionary")

if "price" not in book:
    print("'price' key does not exist in book dictionary")
print()

# ============================================================================
# 8. NESTED DICTIONARIES
# ============================================================================

# Dictionary containing other dictionaries
company = {
    "name": "Tech Corp",
    "location": "Lahore",
    "employees": {
        "emp1": {"name": "Ahmed", "salary": 50000},
        "emp2": {"name": "Fatima", "salary": 55000},
        "emp3": {"name": "Hassan", "salary": 52000}
    }
}

print("Nested dictionary:")
print(f"Company: {company['name']}")
print(f"First employee: {company['employees']['emp1']['name']}")
print()

# ============================================================================
# 9. DICTIONARY COMPREHENSION
# ============================================================================

# Create dictionary using comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create dictionary with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Create dictionary from two lists
names = ["Ali", "Sara", "Ahmed"]
ages = [20, 22, 21]
people = {name: age for name, age in zip(names, ages)}
print(f"People: {people}")
print()

# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Counting occurrences
text = "hello world"
char_count = {}
for char in text:
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")

# Example 2: Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # Works in Python 3.5+
print(f"Merged dictionary: {merged}")

# Example 3: Inverting a dictionary (swap keys and values)
original = {"apple": "fruit", "carrot": "vegetable"}
inverted = {value: key for key, value in original.items()}
print(f"Inverted: {inverted}")
print()

# ============================================================================
# 11. DICTIONARY VS OTHER DATA STRUCTURES
# ============================================================================

print("Comparison:")
print("Lists: Ordered, indexed by numbers [0,1,2...]")
print("Tuples: Immutable, ordered, indexed by numbers")
print("Dictionaries: Key-value pairs, mutable, indexed by keys")
print("Sets: Unordered, unique elements, no key-value pairs")
print()

# ============================================================================
# 12. IMPORTANT NOTES
# ============================================================================

print("""
KEY POINTS ABOUT DICTIONARIES:
1. Dictionaries are MUTABLE (can be modified)
2. Keys must be IMMUTABLE (strings, numbers, tuples)
3. Values can be ANY data type (int, str, list, dict, etc.)
4. Duplicate keys are not allowed; later value overwrites earlier one
5. Dictionaries are ORDERED as of Python 3.7+
6. Dictionaries have O(1) average lookup time - very efficient
7. Use {**dict1, **dict2} to merge dictionaries in Python 3.5+
8. Use dict1 | dict2 to merge dictionaries in Python 3.9+
""")
