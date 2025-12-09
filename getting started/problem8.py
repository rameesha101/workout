"""Problem 8: Write a function istrcmp to compare two strings, ignoring the case."""
def istrcmpr(a,b):
    return a.lower()==b.lower()

print(istrcmpr("pYTHon","PYTHON"))
print(istrcmpr('LaTeX', 'Latex'))
print(istrcmpr('a', 'b'))