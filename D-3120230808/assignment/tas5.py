def increment_digits(digits):
    num = 1  
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += num
        num = digits[i] // 10
        digits[i] %= 10 
        if num == 0:
            break
    if num > 0:
        digits.insert(0, num) 
    return digits

digits = [1, 2, 3]
result = increment_digits(digits)
print(result)

digits = [4,3,2,1]
result = increment_digits(digits)
print(result)

digits = [9]
result = increment_digits(digits)
print(result)

