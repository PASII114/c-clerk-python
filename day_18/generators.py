import time


def generate_numbers():
    yield 10
    yield 11
    yield 12
    yield 15


gen = generate_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def create_large_list(n):
    return list(range(n))

def create_large_list_yield(n):
    for i in range(n):
        yield i

stat_time = time.time()
print(f"List Start Time - {stat_time}")
large_lis = create_large_list(10000000)

end_time = time.time()
print(f"List End Time - {end_time}")

yield_start_time = time.time()
print(f"Yield Start Time - {yield_start_time}")
large_list_yield = create_large_list_yield(10000000)

yield_end_time = time.time()
print(f"Yield End Time - {yield_end_time}")

def get_even_num(n):
    result = []
    for i in range(n):
        if i % 2 ==0:
            result.append(i)

    return result

def get_even_num_yield(n):
    for i in range(n):
        if i % 2 == 0:
            yield 1

for x in get_even_num(20):
    print(x)

even_nums = [i for i in range(100) if i % 2 == 0] #list comprehension

even_nums_gen = (i for i in range(100) if i % 2 == 0) #generator expression
