def get_keys_with_value_true(dictionary):
    return [key for key, value in dictionary.items() if value]
print("\nTask 1.1")
dictionary = {
        "a": True,
        "b": False,
        "c": True
    }
print(get_keys_with_value_true(dictionary))
