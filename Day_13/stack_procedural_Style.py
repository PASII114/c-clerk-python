#LIFO Data Structure (Last in First Out)

stack = []
stack2 = []

def push(x):
    stack.append(x)

def pop():

    if len(stack) > 0:
        pop_value = stack[-1]
        del stack[-1]
        return pop_value

    raise Exception("Stack is Empty")



try:
    push(1)
    push(2)
    push(3)
    print(pop())
    print(stack)

except Exception as e:
    print(e)