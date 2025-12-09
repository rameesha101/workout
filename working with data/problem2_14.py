#Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.


def unique(lst,key=lambda x:x):
    seen = set()
    unique_list = []
    for item in lst:
        k = key(item)
        if k not in seen:
            seen.add(k)
            unique_list.append(item)
    return unique_list


print(unique(["python", "java", "Python", "Java"], key=lambda x: x.lower()))

#"python" and "Python" should be treated as the same.so we add s.lower().s.lower() → "python"
# Output: ['python', 'java']