x = input("Enter a word: ").upper()#make a string uppercase

word_without_vowels = ""

# for i in x:
#     if i == "A":
#         continue
#     elif i == "E":
#         continue
#     elif i == "I":
#         continue
#     elif i == "O":
#         continue
#     elif i == "U":
#         continue
#     else:
#         word_without_vowels = word_without_vowels + i
# print(word_without_vowels)


vowels = "AEIOU"
for i in x:
    if i in vowels:
        continue
    else:
        word_without_vowels += i
print(word_without_vowels)