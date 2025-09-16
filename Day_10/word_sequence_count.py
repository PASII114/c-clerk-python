words = []
frequency_count = {}
count = 0

while True:
    user_input = input("Enter a word (press -1 to exit): ")
    if user_input == "-1":
        break

    words.append(user_input)

for word in words:
    if word in frequency_count.keys():
        frequency_count[word] += 1
    else:
        frequency_count[word] = 1


print(frequency_count)