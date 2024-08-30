# Example of a Python set
fruits = {"apple", "banana", "cherry", "orange", "apple", "banana"}

# Printing the set
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Adding an item to the set
fruits.add("mango")
print(fruits)
# Removing an item from the set
fruits.remove("banana")
print(fruits)

# Example of two sets
set_A = {"apple", "banana", "cherry"}
set_B = {"cherry", "orange", "mango"}

# Union of two sets
set_union = set_A.union(set_B)

# Printing the result
print(set_union)  # Output: {'apple', 'banana', 'cherry', 'orange', 'mango'}
