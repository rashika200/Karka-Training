def find_pairs_with_sum(nums, target_sum):
    pairs = []
    seen = set()

    for num in nums:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    
    return pairs

# Sample input
nums = [2, 3, 5, 4, 7, 9, 8, 5]
target_sum = 9
pairs = find_pairs_with_sum(nums, target_sum)

if pairs:
    print("Pairs found:", ', '.join(f"({pair[0]}, {pair[1]})" for pair in pairs))
else:
    print("No pairs found")