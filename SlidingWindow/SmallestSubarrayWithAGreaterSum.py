# Given an array of positive integers and a number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0 if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2 
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
#7, [2, 1, 5, 2, 3, 2]
def smallest_subarray_sum(s, arr):
    windowStart = 0;
    windowSum = 0;
    minLength= float('inf');

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        while windowSum >= s:
          minLength = min(minLength, windowEnd - windowStart + 1)
          windowSum -= arr[windowStart]
          windowStart +=1
          
    if minLength == float('inf'):
      return 0
    return minLength

