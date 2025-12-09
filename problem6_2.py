"""Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

#flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}"""

def flatten_dict(d, prefix=''):
    result = {}
    for key, value in d.items():

        #create new key by joining prefix and current key
        if prefix=='':
            new_key = key
        else:
            new_key = prefix + '.' + key

    #if value is a dictionary, recursively flatten it
        if isinstance(value, dict):
            inner = flatten_dict(value, new_key)
            result.update(inner)      #add inner dictionary to result
        else:
            result[new_key] = value   #store the final key-value pair
    return result



# Example usage
nested_dict = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
flattened = flatten_dict(nested_dict)
print(flattened)  