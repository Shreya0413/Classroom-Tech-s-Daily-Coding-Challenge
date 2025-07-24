#Question

#You are given a string s, which may contain letters (uppercase or lowercase), digits, spaces, and special characters.

#Your task is to:
#
#Remove all characters except alphabets and digits.
#Convert all uppercase letters to lowercase.
#Check if the cleaned-up string is a palindrome.
#A palindrome is a string that reads the same backward as forward.
#
#Input Format
#
#A single line containing the string s.
#Constraints
#
#1 ≤ |s| ≤ 10^5
#The string may contain letters, digits, spaces, and special characters like @, #, ., etc.
#Output Format
#
#Print "YES" if the cleaned string is a palindrome.
#Print "NO" otherwise.
#Sample Input 0
#
#A man, a plan, a canal: Panama
#Sample Output 0
#
#YES

#Code

s = input()
cleaned = ''
for c in s:
    if c.isalnum():
        cleaned += c.lower()
if cleaned == cleaned[::-1]:
    print("YES")
else:
    print("NO")
