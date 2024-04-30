def how_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = result + [num]
            return memo[target_sum]

    memo[target_sum] = None
    return None

# Example usage:
target_sum = 7
numbers = [2, 3]

result = how_sum(target_sum, numbers)
print(f"How to sum {target_sum} using numbers {numbers}? {result}")
