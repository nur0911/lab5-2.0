def get_elements_with_no_more_than_two_occurrences(input_list):
    result = []
    for item in input_list:
        if input_list.count(item) <= 2 and item not in result:
            result.append(item)
    return result
print("\nTask 1.4")
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
print(get_elements_with_no_more_than_two_occurrences(input_list))
