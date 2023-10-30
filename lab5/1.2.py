def get_unique_elements(input_list):
    return [item for item in input_list if input_list.count(item) == 1]
print("\nTask 1.2")
input_list = [1, 2, 3, 1, 2, 4]
print(get_unique_elements(input_list))