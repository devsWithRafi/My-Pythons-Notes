# Python Basics Reference Guide - Essential Operations
# =====================================================

# STRING OPERATIONS
# =================

# 1. STRING REVERSING
text = "hello"
reversed_text = text[::-1]  # "olleh"
# Alternative methods:
reversed_text2 = ''.join(reversed(text))
reversed_text3 = ""
for char in text:
    reversed_text3 = char + reversed_text3

# 2. STRING LENGTH
text = "python"
length = len(text)  # 6

# 3. CHARACTER COUNTING & REPETITION
text = "programming"

# Count specific character
count_r = text.count('r')  # 2
count_m = text.count('m')  # 2

# Count all characters (frequency)
from collections import Counter
char_count = Counter(text)
# Output: Counter({'r': 2, 'm': 2, 'g': 2, 'p': 1, 'o': 1, 'a': 1, 'n': 1, 'i': 1})

# Manual character counting
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

# Find most repeated character
most_common = max(char_count, key=char_count.get)

# 4. STRING CASE OPERATIONS
text = "Hello World"
upper_text = text.upper()      # "HELLO WORLD"
lower_text = text.lower()      # "hello world"
title_text = text.title()     # "Hello World"
swapped = text.swapcase()     # "hELLO wORLD"
capitalized = text.capitalize()  # "Hello world"

# 5. STRING CHECKING METHODS
text = "Python123"
print(text.isalnum())    # True (alphanumeric)
print(text.isalpha())    # False (contains numbers)
print(text.isdigit())    # False (contains letters)
print(text.islower())    # False
print(text.isupper())    # False
print("123".isdigit())   # True
print("abc".isalpha())   # True

# 6. STRING SEARCHING & FINDING
text = "Python programming is fun"
index = text.find("gram")        # 10 (returns -1 if not found)
rindex = text.rfind("ing")       # 16 (last occurrence)
starts = text.startswith("Py")   # True
ends = text.endswith("fun")      # True
contains = "gram" in text        # True

# 7. STRING SPLITTING & JOINING
text = "apple,banana,cherry"
fruits = text.split(",")         # ['apple', 'banana', 'cherry']
rejoined = " | ".join(fruits)    # "apple | banana | cherry"

# Split by whitespace
sentence = "Hello world python"
words = sentence.split()         # ['Hello', 'world', 'python']

# 8. STRING CLEANING
text = "  Hello World  "
cleaned = text.strip()           # "Hello World"
left_clean = text.lstrip()       # "Hello World  "
right_clean = text.rstrip()      # "  Hello World"
no_spaces = text.replace(" ", "") # "HelloWorld"

# 9. STRING SLICING
text = "Python"
first_char = text[0]             # "P"
last_char = text[-1]             # "n"
first_three = text[:3]           # "Pyt"
last_three = text[-3:]           # "hon"
middle = text[1:-1]              # "ytho"
every_second = text[::2]         # "Pto"

# LIST OPERATIONS
# ===============

# 10. LIST BASICS
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# List length
length = len(numbers)            # 5

# Adding elements
fruits.append("orange")          # Add to end
fruits.insert(1, "mango")        # Insert at index 1
fruits.extend(["grape", "kiwi"]) # Add multiple

# Removing elements
fruits.remove("banana")          # Remove by value
popped = fruits.pop()            # Remove and return last
popped_index = fruits.pop(0)     # Remove and return at index
del fruits[1]                    # Delete by index

# 11. LIST SEARCHING
numbers = [1, 2, 3, 2, 4, 2, 5]
index = numbers.index(3)         # 2 (first occurrence)
count = numbers.count(2)         # 3 (occurrences)
exists = 3 in numbers           # True

# 12. LIST SORTING
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_asc = sorted(numbers)     # [1, 1, 2, 3, 4, 5, 9] (new list)
numbers.sort()                   # Sort in place (ascending)
numbers.sort(reverse=True)       # Sort descending

# Sort strings
words = ["banana", "apple", "cherry"]
words.sort(key=len)              # Sort by length

# DICTIONARY OPERATIONS
# ====================

# 13. DICTIONARY BASICS
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values
name = person["name"]            # "John"
age = person.get("age", 0)       # 30 (with default)

# Adding/updating
person["job"] = "Developer"      # Add new key
person.update({"age": 31, "country": "USA"})  # Update multiple

# Dictionary methods
keys = person.keys()             # dict_keys(['name', 'age', 'city', 'job', 'country'])
values = person.values()         # dict_values([...])
items = person.items()           # dict_items([('name', 'John'), ...])

# Check existence
has_name = "name" in person      # True
has_salary = "salary" in person  # False

# LOOP PATTERNS
# =============

# 14. COMMON LOOP PATTERNS
# Loop with index
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Loop through dictionary
person = {"name": "John", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]           # [1, 4, 9, 16, 25]
evens = [x for x in numbers if x % 2 == 0]  # [2, 4]

# FILE OPERATIONS
# ==============

# 15. READING FILES
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open("file.txt", "r") as f:
    lines = f.readlines()

# 16. WRITING FILES
# Write text
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line\n")

# Write list of lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# INPUT VALIDATION
# ================

# 17. USER INPUT VALIDATION
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        print(f"Please choose from: {', '.join(valid_choices)}")

# NUMBER OPERATIONS
# =================

# 18. COMMON NUMBER OPERATIONS
import math

num = 16
square_root = math.sqrt(num)     # 4.0
power = pow(2, 3)                # 8
absolute = abs(-5)               # 5
rounded = round(3.7)             # 4
ceiling = math.ceil(3.2)         # 4
floor = math.floor(3.8)          # 3

# Check if number is even/odd
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

# UTILITY FUNCTIONS
# =================

# 19. USEFUL UTILITY FUNCTIONS
def remove_duplicates(lst):
    return list(set(lst))

def find_max_min(lst):
    return max(lst), min(lst)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 20. DATE AND TIME
from datetime import datetime, date

current_time = datetime.now()
current_date = date.today()
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")

# EXAMPLE USAGE SCENARIOS
# =======================

# Example 1: Analyze text
def analyze_text(text):
    return {
        'length': len(text),
        'words': len(text.split()),
        'vowels': count_vowels(text),
        'most_common_char': max(Counter(text.lower()), key=Counter(text.lower()).get),
        'is_palindrome': is_palindrome(text)
    }

# Example 2: Process list of numbers
def process_numbers(numbers):
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
        'unique_count': len(set(numbers)),
        'duplicates': [x for x in set(numbers) if numbers.count(x) > 1]
    }

# Example 3: Clean and validate data
def clean_user_data(data_list):
    cleaned = []
    for item in data_list:
        if isinstance(item, str):
            cleaned.append(item.strip().title())
        elif isinstance(item, (int, float)):
            cleaned.append(item)
    return cleaned

print("Python Basics Reference Guide - Ready to use!")
print("Tip: Use Ctrl+F to quickly search for specific operations!")