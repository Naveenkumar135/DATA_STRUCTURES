from collections import deque


class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,data):
        self.buffer.appendleft(data)

    def is_empty(self):
        return len(self.buffer) == 0
    
    def dequeue(self):
        if not self.is_empty():
            item = self.buffer.pop()
            return item
        print("queue is empty")
    
    def get_len(self):
        return len(self.buffer)
    
    def print(self):
        for item in self.buffer:
            print(item)
    

# if __name__ == "__main__":

#     test = Queue()
#     test.dequeue()
#     test.enqueue(1)
#     test.enqueue(4)
#     test.dequeue()
#     test.print()
#     length = test.get_len()
#     print(length)

food_order_queue = Queue()
import time,threading
def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()





    
