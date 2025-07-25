#QUESTION
#You are given a list of N positive integers. Your task is to find the Greatest Common Divisor (GCD) of all the numbers in the list.

#The GCD of a list of numbers is the largest positive integer that divides each of them without leaving a remainder.

#Input Format

#The first line contains a single integer N — the number of elements in the list.
#The second line contains N space-separated positive integers.
#Constraints
#
#2 ≤ N ≤ 10^5
#1 ≤ Ai ≤ 10^12
#Output Format

#Print a single integer — the GCD of all the numbers in the list.
#Sample Input 0
#
#3
#12 18 24
#Sample Output 0
#
#6
#Explanation 0
#
#GCD(12, 18, 24) = 6.
#
#CODE

def gcd_list(a, b):
    if b == 0:
        return a
    return gcd_list(b, a % b)

n = int(input())
l = list(map(int, input().split()))

result_list = l[0]  
for i in range(1, len(l)):
    result_list = gcd_list(result_list, l[i])  

print(result_list)
