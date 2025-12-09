"""Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.

unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}"""

def unflatten_dict(d):          # Function to unflatten a dictionary
    result = {}                 # Initialize an empty dictionary to hold the result
    
    for key, value in d.items():    # Iterate through each key-value pair in the input dictionary
        parts = key.split('.')      # Split the key by '.' 
        current = result          
        
        for part in parts[:-1]:
           current=current.setdefault(part, {})
        
        current[parts[-1]] = value

    return result
print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
