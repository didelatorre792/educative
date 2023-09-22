#Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
#Remember to just focus on length if theyre not asking for the string itself
def longest_substring_with_k_distinct(str1, k):
  windowStart = 0
  maxLength = 0
  charFrequency = {}
  for windowEnd in range(len(str1)):
    rightChar = str1[windowEnd];
    if rightChar not in charFrequency:
      charFrequency[rightChar] = 0;
    charFrequency[rightChar] +=1;
    
    while len(charFrequency) > k:
      leftChar = str1[windowStart]
      charFrequency[leftChar] -=1
      if charFrequency[leftChar] == 0:
        del charFrequency[leftChar]
      windowStart +=1
    maxLength = max(maxLength, (windowEnd-windowStart+1))
      
  return maxLength;
      

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 10)))


main()
