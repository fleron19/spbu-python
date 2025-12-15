import random 
from math import floor

class Walker:
    def __init__(self, pairs: list[tuple[str, float]]):
        self.pairs = pairs
        self.psum = 0
        self.pairsd = {}

        self.num = len(self.pairs)

        for i in range(self.num):
            self.psum += pairs[i][1]
            self.pairsd[self.pairs[i][0]] = self.pairs[i][1]

        if (self.psum != 1):
            raise Exception("Error: probabilities must add up to 1")

        self.new_pairs = []
        self.avg = 1 / self.num
        for pair in self.pairs:
            self.new_pairs.append([pair[0], self.avg])
        
        # storing tuples where 1st element is donor, 2nd is recepient, 3rd is barier value
        self.table = []
        self.recepients = [] 
        self.donors = []
        for i in range(self.num):
            if self.pairs[i][1] > self.new_pairs[i][1]:
                self.recepients.append(self.new_pairs[i])
            elif self.pairs[i][1] < self.new_pairs[i][1]:
                self.donors.append(self.new_pairs[i])
    
        while (self.recepients or self.donors):
            self.recepients[0][1] += self.donors[0][1] - self.pairsd[self.donors[0][0]]
            remain = self.avg - (self.donors[0][1] - self.pairsd[self.donors[0][0]])
            self.table.append([self.donors[0][0], self.recepients[0][0], len(self.table) * self.avg + remain])
            self.donors.pop(0)
            if self.recepients[0][1] > self.pairsd[self.recepients[0][0]]:
                self.donors.append(self.recepients.pop(0))
            elif self.recepients[0][1] == self.pairsd[self.recepients[0][0]]:
                self.recepients.pop(0)
        
        self.table.append([self.table[-1][1], self.table[0][0], 1])
    def get_random(self) -> str:
        value = random.random()
        row_num = floor(self.num * value)
        row = self.table[row_num]
        if value < row[2]:
            return row[0]
        elif value > row[2]:
            return row[1]



