'''
Created on Oct 28, 2015

@author: zimmydoom
'''

import networkx as nx
import random
from numpy.random import choice as nrandom



def read_dataset(self):
    """  takes the node data from a GML file and creates a simple 
         list of node ids.
    """
    node_list= []
    return node_list




def generate_execution(self,comcycles,rtt_matrix, nodelist):
    """ takes a list of nodes on a network and generates 
       a list of tuples  (a,b) representing a message between node a and node b
       an empty tuple represents a decision point.
       There are comcycles = decision points.
    """
    execution_list = []
    while comcycles > 0:
        for node in nodelist:
            cycle_counter = 0
            how_many_messages = random.choice(nodelist)
            while cycle_counter <= how_many_messages:
                receiver =  random.choice(nodelist)
                if receiver == node:
                    receiver = random.choice(nodelist)
                execution_list.append((node[0],receiver[0]))
                #cycle_counter += rtt_matrix[node[0]][receiver[0]] #simular el tiempo que pasa llegando mensajes
                cycle_counter += 1
        execution_list.append(())
        execution_list.append(self.make_winner_list(len(nodelist)))
        comcycles -= 1
        
    return execution_list


def make_winner_list(self,size):
    """out of a list of size size selects a random number of them with a probability (num + 1)/ (size + 5)
    
    """
    winner_list = []
    numbers = range(1,size)
    for num in numbers:
        p = (num + 1)/ (size + 5)
        ap = 1 - p
        coin = nrandom([0,1],[ap,p])
        if coin == 1:
            winner_list.append(num)
    return winner_list
    
