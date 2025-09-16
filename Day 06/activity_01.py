word = input("Enter a word: ").upper()

if word == word[::-1]:
    print(f"{word} is a Palindrome Word.")

else:
    print(f"{word} is not a Palindrome Word.")

#Palindrome - a word, sentence, verse, or even number that reads the same backward or forward