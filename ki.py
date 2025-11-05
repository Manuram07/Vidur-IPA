def kadane(arr):
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage:
nums = [5,-3,5]
print(kadane(nums))  # Output: 6 (subarray [4, -1, 2, 1])
