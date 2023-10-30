def get_perfect_squares(input_list):
    perfect_squares = [item for item in input_list if int(item ** 0.5) ** 2 == item]
    return perfect_squares
print("\nTask 3.11")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_perfect_squares(input_list))