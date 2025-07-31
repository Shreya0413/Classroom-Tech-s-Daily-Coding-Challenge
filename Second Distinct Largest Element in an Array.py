#Question
#
#Problem
#Submissions
#Leaderboard
#Discussions
#You are given an array of integers (which may contain duplicate values, negative numbers, and very large or small values).
#
#Your task is to find the second largest distinct element in the array.
#
#If there is no second distinct largest element (because all elements are the same), print "NO".
#
#Important:
#
#The "second largest" must be different from the largest.
#Duplicates do not count as different elements.
#Input Format
#
#The first line contains an integer n — the number of elements in the array.
#The second line contains n space-separated integers.
#Constraints
#
#2 ≤ n ≤ 10^5
#-10^9 ≤ arr[i] ≤ 10^9
#Output Format
#
#Print the second largest distinct element.
#If it does not exist, print NO.
#Sample Input 0
#
#6
#5 3 9 1 9 5
#Sample Output 0
#
#5
#
#CODE

n = int(input())
arr = list(map(int, input().split()))

first_max = float('-inf')
second_max = float('-inf')

for num in arr:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num

if second_max == float('-inf'):
    print('NO SECOND LARGEST')
else:
    print(second_max)
