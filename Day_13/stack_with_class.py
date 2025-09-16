class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self, element):
        self.__stack_list.append(element)

    def pop(self):
        if len(self.__stack_list) > 0:
            pop_value = self.__stack_list[-1]
            del self.__stack_list[-1]
            return pop_value

        raise Exception ("Stack is Empty")

    def print_values(self):
        if len(self.__stack_list) > 0:
            print(f"Stack values after popping - {self.__stack_list}")

        else:
            print("Stack is Empty")

class AddingStack(Stack): #Inheritance

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, element):
        Stack.push(self, element)   #method overriding
        self.__sum += element

    def pop(self):
        pop_value = Stack.pop(self)
        self.__sum -= pop_value
        return pop_value

    def get_sum(self):
        return self.__sum

class CountingStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def pop(self):
        self.__count += 1
        return Stack.pop(self)

    def get_count(self):
        return self.__count

stack_1 = Stack()
stack_2 = Stack()

try:
    stack_1.push(1)
    stack_1.push(2)
    stack_1.push(3)

    print(f"Popping value of Stack 1 is {stack_1.pop()}")
    stack_1.print_values()

    stack_2.push(10)
    stack_2.push(20)
    stack_2.push(30)

    print(f"Popping value of Stack 2 is {stack_2.pop()}")
    stack_2.print_values()

except Exception as e:
    print(e)


counting_stack = CountingStack()

for i in range(20):
    counting_stack.push(i)
    counting_stack.pop()

print(counting_stack.get_count())