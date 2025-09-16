book_names = ["Science", "Maths", "history", "IT", "commerce", "SFT", 18]

print(book_names[0])

book_names[6] = "ET" #Replace the value of index at 6

print(book_names)

print(len(book_names))

print(book_names[-1])#Access the last element

print(book_names[-2])#Access the element before last one

for book_name in book_names:
    print(book_name)

book_names.append("SILO")
book_names.insert(2, "Good habits")

del book_names[0]
print(book_names)

# print(help(book_names))#print all the available methods


if "history" in book_names:
        book_names.remove("history")#remove from value

book_names.pop(0)#remove from index

print(book_names)