'''
Created on Oct 28, 2015

@author: zimmydoom
'''

import networkx as nx
import random



def read_dataset(self):
    """  takes the node data from a GML file and creates a simple 
         list of node ids.
    """
    node_list= []
    return node_list




def generate_execution(self,comcycles,rtt_matrix, nodelist, cycle_length):
    """ takes a list of nodes on a network and generates 
       a list of tuples  (a,b) representing a message between node a and node b
       an empty tuple represents a decision point.
       There are comcycles = decision points.
    """
    execution_list = []
    cyclen = cycle_length
    while comcycles > 0:
        for node in nodelist:
            cycle_counter = 0
            while cycle_counter <= cyclen:
                receiver =  random.choice(nodelist)
                if receiver == node:
                    receiver = random.choice(nodelist)
                execution_list.append((node[0],receiver[0]))
                cycle_counter += rtt_matrix[node[0]][receiver[0]] #simular el tiempo que pasa llegando mensajes
                cycle_counter += 1
        execution_list.append(())
        comcycles -= 1
        
    return execution_list

