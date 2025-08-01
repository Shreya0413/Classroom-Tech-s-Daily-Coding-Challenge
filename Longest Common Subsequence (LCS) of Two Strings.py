#QUESTIONS
#
#Given two strings A and B, find the length of their Longest Common Subsequence (LCS).
#
#A subsequence of a string is obtained by deleting zero or more characters without changing the relative order of the remaining characters.
#The Longest Common Subsequence is the longest sequence that is a subsequence of both strings.
#Input Format
#
#The first line contains the string A.
#The second line contains the string B.
#Constraints
#
#1 ≤ |A|, |B| ≤ 1000
#
#Strings consist of lowercase English letters only.
#
#Output Format
#
#Print a single integer — the length of the longest common subsequence.
#Sample Input 0
#
#abcde
#ace
#Sample Output 0
#
#3
#
#CODE

A = input().strip()
B = input().strip()

i, j = 0, 0   # pointers for A and B
count = 0     # length of LCS

while i < len(A) and j < len(B):
    if A[i] == B[j]:
        count += 1
        j += 1   # move forward in B
    i += 1       # always move forward in A

print(count)
