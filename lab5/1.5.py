def get_words_from_string(input_string):
    words = input_string.split()
    return words
print("\nTask 1.5")
string = "This is a string with several words."
print(get_words_from_string(string))