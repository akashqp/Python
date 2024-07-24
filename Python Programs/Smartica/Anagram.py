# Input Specification:
# Input 1: the first string
# Input 2: the second string
# Output Specification:
# Return "Yes" if they are anaagrams, else return "No"
# Don't use any inbuilt functions

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return "No"
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return "No"
    return "Yes"

s1 = "listen"
s2 = "silent"
print(isAnagram(s1, s2))

s1 = "hello"
s2 = "world"
print(isAnagram(s1, s2))