def get_unique_elements_with_count(input_list):
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
print("\nTask 2.6")
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
print(get_unique_elements_with_count(input_list))