class RingBuffer:
  def __init__(self, capacity=0):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0    
      self.storage[self.current] = item
    if self.current <= self.capacity:
      self.storage[self.current] = item
      self.current += 1

 
    
  # def append(self, item):
  #   self.storage[self.current] = item
  #   if self.current < self.capacity - 1:
  #     self.current += 1
  #   else:
  #     self.current = 0
    
  def get(self):
    return [element for element in self.storage if element != None]


# self.storage is array itself
# self.current is the index
# self.capacity is size of array or len of self.storage
