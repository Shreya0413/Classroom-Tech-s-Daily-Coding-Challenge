#Question
#
#You are given an array of integers. Your task is to remove all duplicate elements while preserving the order of first occurrence.
#
#Print the resulting array of unique elements in the order they first appeared in the input.
#
#Input Format
#
#The first line contains an integer n — the number of elements in the array.
#The second line contains n space-separated integers.
#Constraints
#
#1 ≤ n ≤ 10^5
#-10^9 ≤ arr[i] ≤ 10^9
#Output Format
#
#Print a single line with the unique elements separated by spaces, in their original order of first appearance.
#
#Sample Input 0
#
#8
#1 2 3 2 1 4 5 3
#Sample Output 0
#
#1 2 3 4 5
#Sample Input 1
#
#5
#10 20 30 40 50
#Sample Output 1
#
#10 20 30 40 50
#
#Code
#
n = int(input())
arr = list(map(int, input().split()))

res = set()

for num in arr:
    if num not in res:
        res.add(num) 
        print(num, end=' ')

