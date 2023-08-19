def largest_subsequent_difference(nums_list):
    largest_difference = float("-inf")
    
    for i in range(len(nums_list) - 1):
        difference = nums_list[i + 1] - nums_list[i]
        if difference > largest_difference:
            largest_difference = difference
    
    return largest_difference

# Sample input
nums_list = [2, 5, 8, 1, 9, 3, 7]
output = largest_subsequent_difference(nums_list)
print(output)