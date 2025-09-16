class NumberGenerator:

    def __init__(self, num: int):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration

        self.current += 1
        return self.current

number_gen = NumberGenerator(10)

number_gen_itr = iter(number_gen)
print(next(number_gen_itr))

# for num in NumberGenerator(100):
#     print(num)