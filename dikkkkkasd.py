# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'job': 'Engineer'
}

# Access values in the dictionary
print("Name:", my_dict['name'])  # Accessing a specific key

# Get a list of all keys in the dictionary
keys = my_dict.keys()
print("Keys:", list(keys))

# Get a list of all values in the dictionary
values = my_dict.values()
print("Values:", list(values))

# Check if a key exists in the dictionary
print("Is 'age' in the dictionary?", 'age' in my_dict)

# Get the number of key-value pairs in the dictionary
print("Number of items in the dictionary:", len(my_dict))

# Add a new key-value pair to the dictionary
my_dict['country'] = 'USA'

# Update an existing key's value
my_dict['age'] = 31

# Remove a key from the dictionary
del my_dict['job']

# Remove all items from the dictionary
my_dict.clear()

# Copy the dictionary
copy_dict = my_dict.copy()

# Create a new dictionary with keys from a list and a default value
keys_list = ['apple', 'banana', 'cherry']
default_value = 0
new_dict = dict.fromkeys(keys_list, default_value)

# Get the value for a key and provide a default value if the key doesn't exist
value = my_dict.get('name', 'Default Name')

# Get a list of key-value pairs as tuples
items = my_dict.items()
print("Items:", list(items))

# Get and remove the last key-value pair as a tuple
last_item = my_dict.popitem()

