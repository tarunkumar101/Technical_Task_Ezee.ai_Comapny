def string_replacing(input_string):
    cleaned_string = ''
    for char in input_string:
        if char.isdigit() or not char.isalnum():
            cleaned_string += ' '  
        else:
            cleaned_string += char

    return cleaned_string


input_string = input()
result = string_replacing(input_string)
print("Original String:", input_string)
print("String after replacement:", result)
