from listQueue import ListQueue
import threading
import time
q=ListQueue()
class Producer:
    def __init__(self, items):
        self.__alive=True
        self.items=items
        self.pos=0
        #self.queue_p=ListQueue()
        self.worker=threading.Thread(target=self.run)

    def get_item(self):
        if self.pos<len(self.items):
            item=self.items[self.pos]
            self.pos+=1
            return item
        else:
            return None
        
    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item=self.get_item()
                print("Arrived:",item)
                q.enqueue(item)
            else:
                break
        print("Producer is dying..")


    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive=False
        self.worker.join()



class Consumer:
    def __init__(self):
        self.__alive=True
        #
        self.worker=threading.Thread(target=self.run)

    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:
                item=q.dequeue()
                print("Boarding:",item)
            else:
                break
        print("Consumer is dying..")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive=False
        self.worker.join()

if __name__ == "__main__":
    
    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names = []
    for c in customers:
        names.append(c[1])

    producer = Producer(names)

    # Priority 
#    producer = Producer(customers)
    consumer = Consumer()  
    producer.start()
 
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()
