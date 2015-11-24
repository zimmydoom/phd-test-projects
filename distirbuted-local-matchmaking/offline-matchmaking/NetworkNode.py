
import thread
import time
import random

class NetworkNode:
    CR_CONSTANT = 1
    
    
    def __init__(self,name, starting_CR,minimum_CR):
        self.name = name
        self.CR = starting_CR
        self.minimum = minimum_CR
        self.CR_CONSTANT = 20
        self.whoIheard = []
        self.neighbors = []
        self.NOR_CONSTANT = 20
        
    def calculate_new_cr(self, result): #result es 1 o 0 1 es ganar 0 es perder
        expected =self.expected_result()
        if self.name == 19 and result == 1:
            print 'CR antes :'
            print repr(self.CR)
            print repr(expected)
        self.CR = self.CR + (result - expected)*self.CR_CONSTANT
        if self.name == 19 and result == 1:
            print 'CR nuevo :'
            print repr(self.CR)
        if self.CR < self.minimum:
            self.CR = self.minimum
        #if self.name == 19 and result ==1:
        #    print 'Escuche a :'
        #    print repr(self.whoIheard)
        self.whoIheard = [] #forget this round
        return self.CR
        
    def heard_someone(self, other_cr):
        self.whoIheard.append(other_cr)
    
        
    def expected_result(self):
        how_many_above = self.count_greater_list()
        how_many_below = self.count_lower_list()
        sup = self.supreme_heard()
        if how_many_above == how_many_below == 0: #si estoy solo
            alfa = self.NOR_CONSTANT
            beta = 2
        elif how_many_above <= how_many_below:
            alfa = float(1)/float((sup - self.CR + 1)) * self.NOR_CONSTANT  # Aqui puede haber una constante 
            beta = 2
        else:
            alfa = 2
            beta = float(sup - self.CR) / float(self.NOR_CONSTANT)
        mean= random.betavariate(alfa,beta)
        return mean
    
    def count_greater_list(self): #eventualmente optimizar esto
        counter = 0
        for x in self.whoIheard:
            if x > self.CR:
                counter = counter + 1
        return counter
    
                
    def count_lower_list(self):
        counter = 0
        for x in self.whoIheard:
            if x < self.CR:
                counter = counter + 1
        return counter
    
    def supreme_heard(self):
        supreme = max(self.whoIheard)
        if supreme > self.CR:
            return supreme
        else:
            return self.CR
        