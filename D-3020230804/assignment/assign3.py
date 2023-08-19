def word_frequency(input_str):
    words = input_str.split()
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

# Sample input
input_str = "the quick brown fox jumps over the lazy dog the quick brown fox"
frequency_dict = word_frequency(input_str)
print(frequency_dict)