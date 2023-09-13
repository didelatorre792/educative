# Problem Statement
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

#edge cases: negative subarrrays
# 
#2, [2, 3, 4, 1, 5]
#3, [2, 1, 5, 1, 3, 2]
def max_sub_array_of_size_k(k, arr):
    currSubArray = 0
    currSum = 0;
    i = 0;
    maxSum = 0;
    while (i < (len(arr))):
        currSum += arr[i]
        currSubArray = currSubArray + 1
        i = i + 1
        if currSubArray == k:
                maxSum = max(currSum, maxSum)
                currSum = currSum - arr[i-k]
                currSubArray = currSubArray - 1
    if maxSum == 0: 
      return -1 
    else:
      return maxSum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

# Time Complexity
# The time complexity of the above algorithm will be O(N)

# Space Complexity
# The algorithm runs in constant space O(1)