def convert_odd_length_strings(input_string):
    if len(input_string) % 2 == 1:
        midpoint = len(input_string) // 2
        converted_string = input_string[:midpoint].upper() + input_string[midpoint:].lower()
        return converted_string
    else:
        return input_string


input_string =input()
result = convert_odd_length_strings(input_string)

print("Original Odd String:", input_string)
print("String after conversion:", result)