def array_operation(nums, operation):
    if operation == "Add":
        total = sum(sum(row) for row in nums)
        return total
    elif operation == "String":
        value = [num for sublist in nums for num in sublist]
        return str(value)
    else:
        return "Invalid operation"

nums1 = [[1, 2], [3, 4]]
operation1 = "Add"
print(array_operation(nums1, operation1)) 

nums2 = [[23, 98], [42, 70]]
operation2 = "String"
print(array_operation(nums2, operation2))  