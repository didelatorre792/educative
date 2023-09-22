# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as 
# possible to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

def fruits_into_baskets(fruits):
    windowStart = 0;
    maxFruit = 0;
    distFruit = {};
    for windowEnd in range(len(fruits)):
        rightFruit = fruits[windowEnd];
        if rightFruit not in distFruit:
            distFruit[rightFruit] = 0;
        distFruit[rightFruit] +=1;
        
        while len(distFruit) > 2:
            leftFruit = fruits[windowStart]
            distFruit[leftFruit] -=1
            if distFruit[leftFruit] == 0:
                del distFruit[leftFruit]
                
            windowStart +=1
        
        maxFruit = max(maxFruit, (windowEnd - windowStart + 1))  
    return maxFruit      
      

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()