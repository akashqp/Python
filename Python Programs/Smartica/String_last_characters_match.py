# k1: 4
# k2: 7
# str1: succeed
# str2: crossbreed
# Output: 3
# If end characters after removing k1 and k2 characters are same, then return the length of the common string.

class LastCharactersMatch:
    def last_characters_match(self, k1, k2, str1, str2):
        if str1[k1:] == str2[k2:]:
            return len(str1[k1:])
        return -1
    
# Create object of the class
last_characters_match = LastCharactersMatch()

k1 = 4
k2 = 3
str1 = "application"
str2 = "apple"

# Call the method to find length of common string
print("Length of common string is", last_characters_match.last_characters_match(k1, k2, str1, str2))