from listQueue import ListQueue
import threading
import time
q_1=ListQueue()
q_2=ListQueue()
q_3=ListQueue()
queues=[q_1,q_2,q_3]

class Producer:
    def __init__(self, items):
        self.__alive=True
        self.items=items
        self.pos=0
        #self.queue_p=ListQueue()
        self.worker=threading.Thread(target=self.run)

    def get_item(self):
        if self.pos<len(self.items):
            item=self.items[self.pos][1]
            c_class=self.items[self.pos][0]
            self.pos+=1
            return (item,c_class)
        else:
            return None
        
    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item,c_class =self.get_item()
                
                print("Arrived:",item)
                if c_class=='1':
                    q_1.enqueue(item)
                elif c_class=='2':
                    q_2.enqueue(item)
                else:
                    q_3.enqueue(item)
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
        self.worker=threading.Thread(target=self.run)


    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:
                for queue in queues:
                    if not queue.isEmpty():
                        item=queue.dequeue()
                        print("Boarding:",item)
                        break
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

    producer = Producer(customers)
    consumer = Consumer()  
    producer.start()
 
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()
