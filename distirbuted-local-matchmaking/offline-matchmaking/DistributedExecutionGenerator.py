'''
Created on Oct 28, 2015

@author: zimmydoom
'''


from NetworkNode import NetworkNode
import random
from numpy.random import choice as nrandom



def read_dataset():
    """  takes the node data from a GML file and creates a simple 
         list of node ids.
    """
    node_list= range(0,20)
    return node_list




def generate_execution(comcycles,rtt_matrix, nodelist):
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
                execution_list.append((node,receiver))
                #cycle_counter += rtt_matrix[node[0]][receiver[0]] #simular el tiempo que pasa llegando mensajes
                cycle_counter += 1
        execution_list.append(())
        execution_list.append(make_winner_list(len(nodelist)))
        comcycles -= 1
        
    return execution_list


def make_winner_list(size):
    """out of a list of size size selects a random number of them with a probability (num + 1)/ (size + 5)
    
    """
    winner_list = []
    numbers = range(1,size+1)
    for num in numbers:
        denom = size/4
        pr = float(num+1)/float(size+denom)
        ap = 1 - pr
        print repr(pr)
        coin = nrandom([0,1],1,replace=False,p=[ap,pr])
        print repr(coin)
        if coin[0] == 1:
            winner_list.append(num)
    return winner_list
    

def execute_test(exec_list, node_list):
    CR_list = []
    for x in range(len(node_list)):
        CR_list.append(100)
    main_index = 0
    decision_index = 0
    while main_index < len(exec_list):
        for node in node_list:
            executor = NetworkNode(node,CR_list[node])
            loop_index = main_index
            while exec_list[loop_index] != ():
                 pareja = exec_list[loop_index]
                 if node == pareja[1]: #recibimos un mensae
                    executor.heard_someone(CR_list[pareja[0]])
                 loop_index += 1
            decision_index = loop_index + 1
            if node in exec_list[decision_index]:
                CR_list[node] = executor.calculate_new_cr(1)
            else:
                CR_list[node] = executor.calculate_new_cr(0)
        main_index = decision_index + 1
    return CR_list
    

def main():
    test_nodes = read_dataset()
    print repr(test_nodes)
    ex_list = generate_execution(10,[],test_nodes)
    print repr(ex_list)
    cr_result = execute_test(ex_list,test_nodes)
    print repr(cr_result)
    


if __name__ == '__main__':
   main()
   
     
#def read_rtt_matrix(self,size):