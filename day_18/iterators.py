from typing import List

student_names = ["Kalana", "Pasan", "Dasun"] #iterable


print(type(student_names))
# print(help(student_names))

student_iterator = student_names.__iter__() #calling iterator dunder method to get an iterator
student_iterator2 = iter(student_names)

print(next(student_iterator2))
print(next(student_iterator2))

for student in student_names:
    print(student)


try:
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
except StopIteration as e:
    print(e)


class CountDown: #implementing iterator protocol

    def __init__(self, num: int):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num -= 1
        if self.num == 0:
            raise StopIteration
        return self.num

count_down = CountDown(10)

count_down_itr = iter(count_down)

print(count_down_itr.__next__())
print(count_down_itr.__next__())
print(count_down_itr.__next__())

print("++++++++++++++++++++++++++++++++")

for i in count_down: #Creates an iterator and then calls the next method in the iterator objects
    print(i)


def generate_numbers(n: int) -> List[int]:
    result = []

    for i in range(n):
        result.append(i)

    return result

print("+++++++++++++++++++++++++++++++++++++++++++++++")
for num in generate_numbers(10):
    print(num)

