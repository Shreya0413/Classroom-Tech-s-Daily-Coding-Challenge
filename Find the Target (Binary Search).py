#Question
#You are given a sorted array of integers in non-decreasing order and a target value. Your task is to determine the index of the target in the array using binary search.
#
#If the target exists in the array, print its 0-based index.
#If the target does not exist in the array, print -1.
#Input Format
#
#First line contains an integer n — the size of the array.
#Second line contains n space-separated integers — the elements of the array (sorted in non-decreasing order).
#Third line contains an integer target — the value to search for.
#
#Constraints
#1 ≤ n ≤ 10^5
#-10^9 ≤ arr[i], target ≤ 10^9
#The array is sorted in non-decreasing order.
#Output Format
#Print a single integer — the index of target in the array, or -1 if not found.
#Sample Input 0
#
#8
#-5 -2 0 3 3 3 7 9
#3
#Sample Output 0
#
#3
#Explanation 0
#
#3 is at index 3 (any valid index with value 3 is acceptable if multiple occurrences are present).

#CODE
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(mid)
        exit()
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(-1)
