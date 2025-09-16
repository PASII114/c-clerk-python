try:
    x = int(input("Enter a digit: "))
except (ValueError, ZeroDivisionError):
    print("test", "Hi")

text = 'x'
try:
    while True:
        text = text + text
        print(len(text))
except MemoryError:
    print("Out of memory")