# Input Specification:
# Input 1: the first string
# Input 2: the second string
# Output Specification:
# Return "Yes" if they are anaagrams, else return "No"
# Don't use any inbuilt functions such as sort, sorted, etc.

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return "No"
    count1 = [0] * 256
    count2 = [0] * 256
    for i in range(len(s1)):
        count1[ord(s1[i])] += 1
        count2[ord(s2[i])] += 1
    for i in range(256):
        if count1[i] != count2[i]:
            return "No"
    return "Yes"

s1 = "listen"
s2 = "silent"
print(isAnagram(s1, s2))

s1 = "hello"
s2 = "world"
print(isAnagram(s1, s2))