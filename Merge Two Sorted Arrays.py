#Question
#
#You are given two sorted arrays in non-decreasing order. Your task is to merge them into a single sorted array in non-decreasing order, without using any built-in sort function.
#
#You must maintain the order and efficiently combine both arrays.
#
#Input Format
#
#The first line contains an integer n — the size of the first array.
#The second line contains n space-separated integers — the elements of the first array (sorted).
#The third line contains an integer m — the size of the second array.
#The fourth line contains m space-separated integers — the elements of the second array (sorted).
#Constraints
#
#1 ≤ n, m ≤ 10^5
#-10^9 ≤ arr[i] ≤ 10^9
#Both arrays are already sorted in non-decreasing order.
#Output Format
#
#Print a single line containing the merged sorted array with all elements separated by spaces.
#
#Sample Input 0
#
#5
#1 3 5 7 9
#4
#2 4 6 8
#Sample Output 0
#
#1 2 3 4 5 6 7 8 9
#
#CODE
#
m=int(input())
arr1=list(map(int, input().split()))

n=int(input())
arr2=list(map(int, input().split()))

merge=arr1+arr2 # if arr in [1,2,3,4] and [5,6,7,8] then [1,2,3,4,5,6,7,8] after + but if it is in numpy then[6,8,10,12]

merge.sort()

print(*merge)
