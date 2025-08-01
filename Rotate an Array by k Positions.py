#Question
#
#You are given an array of integers and an integer k. Rotate the array to the right by k positions.
#
#A single rotation to the right means: the last element moves to the first position, and all other elements shift one position to the right.
#If k is larger than the size of the array, rotations wrap around (i.e. perform k % n rotations).
#Your task is to output the final rotated array.
#
#Input Format
#
#The first line contains two integers n and k — the size of the array and the number of positions to rotate.
#The second line contains n space-separated integers — the elements of the array.
#Constraints
#
#1 ≤ n ≤ 10^5
#-10^9 ≤ arr[i] ≤ 10^9
#0 ≤ k ≤ 10^9
#Output Format
#
#Print a single line with the rotated array elements separated by spaces.
#Sample Input 0
#
#5 2
#1 2 3 4 5
#Sample Output 0
#
#4 5 1 2 3
#Explanation 0
#
#After rotating 2 times to the right:
#
#1st rotation: 5 1 2 3 4
#
#2nd rotation: 4 5 1 2 3
#
#CODE
#
n, k = map(int, input().split())
nums = list(map(int, input().split()))

k = k % n  

nums.reverse()

nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])

for i in nums:
    print(i,end=" ")


    

 
1
​
