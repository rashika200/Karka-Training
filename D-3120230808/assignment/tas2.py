def find_majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    count_candidate = 0
    for num in nums:
        if num == candidate:
            count_candidate += 1
    
    if count_candidate > len(nums) // 3:
        return candidate
    else:
        return None 

# Example usage
nums = [3,2,4,4,3,4,3,1,3,4,3]
print(find_majority_element(nums))  
