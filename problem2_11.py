#Problem 11: Write a function dups to find all duplicates in the list.


def dups(lst):
    elements_seen = []
    duplicates = []
    for item in lst:
        if item in elements_seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            elements_seen.append(item)
    return duplicates


print(dups([1, 2, 3, 4, 2, 3, 5, 1]))


# Output: [2, 3, 1]