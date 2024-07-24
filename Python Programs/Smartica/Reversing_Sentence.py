class ReverseSentence:
    def reverse_sentence(self, sentence):
        result = ""
        word = ""
        for i in range(len(sentence)):
            if sentence[i] != " ":
                word += sentence[i]
            else:
                result = word + " " + result
                word = ""
        result = word + " " + result
        return result

reverse_sentence = ReverseSentence()
sentence = input("Enter a sentence: ")
result = reverse_sentence.reverse_sentence(sentence)
print("Reversed sentence is:", result)
