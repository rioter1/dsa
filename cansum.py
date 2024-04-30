def can_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True 
            return True
    
    memo[target_sum] = False
    return False

# Example usage:
target_sum = 7
numbers = [2, 3]

print(f"Can sum {target_sum} using numbers {numbers}? {can_sum(target_sum, numbers)}")