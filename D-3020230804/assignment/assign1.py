def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def max_vowels_word(input_string):
    words = input_string.split()
    max_vowels = 0
    max_vowels_word = ""

    for word in words:
        vowels_count = count_vowels(word)
        if vowels_count > max_vowels:
            max_vowels = vowels_count
            max_vowels_word = word
    
    return f"Maximum vowels are in the word \"{max_vowels_word}\""

# Sample input
input_string = "Hai I'm Niranjan and Im from Nagercoil"
print(max_vowels_word(input_string))