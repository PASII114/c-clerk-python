#take 5 words as inputs and put them in a list
#create a new list with words length greater than 3 characters

word_count = 1
words = []

while word_count <= 5:
    word_input = input("Enter a Word: ")
    words.append(word_input)
    word_count += 1

print(words)
print("###########################################")

words_length_greater_than_3char = [word for word in words if len(word) > 3]
print(words_length_greater_than_3char)

first_letter_multiplied_by_3 = [word[0] * 3 for word in words]
print(first_letter_multiplied_by_3)