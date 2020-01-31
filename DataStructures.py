class Queue:
    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def get_queue(self):
        pass
    def size(self):
        return len(self._queue) 


class Justis:
    def __init__(self, x):
        self.x = x
        self.height = "177cm"
        self.weight = "65kg"
        self.build = "Slim"
        self.hair = "black"
        self.eyes = "brown"
        self.ethnicity = "black"
    def print_var(self):
        print(self.x)
        print(self.height)
        print(self.weight)
        print(self.build)
        print(self.hair)
        print(self.eyes)
        print(self.ethnicity)



Profile = Justis('Profile')
Profile.print_var()





# print(Profile.height)
# print(Profile.weight)


