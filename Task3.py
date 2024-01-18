def find_second_and_fourth_greatest(numbers):
    if len(numbers) < 4:
        return "Error: List has less than 4 numbers."
    sorted_numbers = sorted(numbers, reverse=True)
    second_greatest = sorted_numbers[1]
    fourth_greatest = sorted_numbers[3]
    return second_greatest, fourth_greatest

number_list = list(map(int,input().split()))
result = find_second_and_fourth_greatest(number_list)
print("Original List:", number_list)
print("Second Greatest:", result[0])
print("Fourth Greatest:", result[1])
