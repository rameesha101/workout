def center_align(filename):
        #Read all lines
    with open(filename) as f:
        lines = f.readlines()

    # Find length of the longest line
    longest = 0
    for line in lines:
        length = len(line.strip())
        if length > longest:
            longest = length

    # Print each line centered
    for line in lines:
        text = line.strip()
        spaces = (longest - len(text)) // 2
        print(" " * spaces + text)


# Example taking she.text file
center_align("she.txt")
