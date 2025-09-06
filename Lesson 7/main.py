# Empty Tuple
t1 = ()

# Tuple with integers
t2 = (1, 2, 3)

# Mixed data types
t3 = (1, "Hello", 3.5)

# Nested Tuple
t4 = (1, (2, 3), 4)

# Tuple with single element (note the comma)
t5 = (10,)

# Not Tuple (missing comma) just an integer in parentheses
t6 = (10)  

print(type(t5)) 
print(type(t6))

numbers = (10, 20, 30, 40)
print(numbers[0])  # 10 (first element)
print(numbers[-1]) # 40 (last element)
print(numbers[1:3]) # (20, 30) → slicing 

a = (1, 2, 3)
b = (4, 5)

# Concatenation
print(a + b)  # (1, 2, 3, 4, 5)

# Repetition
print(a * 2)  # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in a) # True
print(6 in a) # False

# Tuple unpacking
person = ("Anay", 13, "UK")
name, age, country = person # If you do more variables than elements, it will raise a Error
print(name)    # Anay
print(age)     # 13
print(country) # UK

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3]) # Output: 5 (in tuples you can do nested indexing like matrix)
print(n_tuple[1][1]) # Output: 4

# HW 1

# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

print(my_tuple[1:5])
print(my_tuple[:2])
print(my_tuple[7:])
print(my_tuple)

# Changing tuple values
my_tuple = list(my_tuple)
for i in range(len(my_tuple)):
    my_tuple[i] = my_tuple[i].upper()

my_tuple = tuple(my_tuple)
print(my_tuple)
