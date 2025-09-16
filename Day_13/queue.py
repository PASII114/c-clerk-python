#FIFO Data Structure (First in First Out)
class QueueError(Exception):
    pass


class Queue:

    def __init__(self):
        self.__queue = []


    def put(self, element):
        self.__queue.insert(0, element)

    def get(self):
        if self.__queue:
            serving_value = self.__queue[-1]
            del self.__queue[-1]

            return serving_value

        raise QueueError

    def get_queue(self):
        return self.__queue


class ChildQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def get_size(self):
        return len(Queue.get_queue(self))


try:
    restaurant_queue = Queue()
    restaurant_queue.put("Amal")
    restaurant_queue.put("Kamal")
    restaurant_queue.put("Nimal")
    restaurant_queue.put("Sunimal")

    print(restaurant_queue.get())
    print(restaurant_queue.get())
    print(restaurant_queue.get())
    print(restaurant_queue.get())

except QueueError as e:
    print(e)

try:
    child_queue = ChildQueue()
    child_queue.put(1)
    print(child_queue.get_size())
except:
    print("Error")