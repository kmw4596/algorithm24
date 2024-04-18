def print_substrings(string):
    last_a_index = -1
    
    for i, char in enumerate(string):
        if char == 'A':
            last_a_index = i
        elif char == 'B':
            if last_a_index != -1:
                print(string[last_a_index:i+1])
                last_a_index += 1
                i = last_a_index

string = "ADBAAEDBA"
print_substrings(string)
