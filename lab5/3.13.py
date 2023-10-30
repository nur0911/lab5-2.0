def get_words_starting_with_vowel(words):
    vowels = "aeiou"
    return [word for word in words if word[0].lower() in vowels]
print("\nTask 3.13")
words = ["apple", "banana", "orange", "bear", "cat"]
print(get_words_starting_with_vowel(words))