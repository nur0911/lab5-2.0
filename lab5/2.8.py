from main import get_prime_numbers
def get_prime_numbers_in_list(input_list):
    max_num = max(input_list)
    prime_numbers = get_prime_numbers(max_num)  # You need to define the 'get_prime_numbers' function.
    return [item for item in input_list if item in prime_numbers]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
print(get_prime_numbers_in_list(input_list))
