# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:07:38 2018

Matt Fleetwood
ECE 485
Winter 2018

Simulator class for simulating a single level of cache.
Simulator reports cache statistics at the end of all address traces.
"""

import cache as c

class simulator(object):
    """A simulator simulates address traces for the cache class"""
    #The simulator accepts a file to determine R/WR (type of access) and the byte being addressed
    
    def __init__(self):
        print('This simulator simulates an L1 cache with a writeback policy. There are 2 modes, 0 and 1, for reading from a file and for receiving inputs from the command line.')
        self.mode = int(input('Enter simulator mode (0 for reading a file and 1 for reading from the command line):'))
        association = int(input('Enter the associativity for the cache to be built:'))
        num_sets = int(input('Enter the number of sets for the cache to be built:'))
        line_size = int(input('Enter the line size for the cache to be built:'))
        self.cache_sim = c.cache(num_sets, association, line_size)
        
        if(self.mode):
            print('Entering command line mode . . .')
        else:
            print('Entering read file mode . . .')
            
    def printStatistics(self):
        self.cache_sim.printStatistics()
        
    #Read from the file, parse the information and send cache access information to cache class

test = simulator()
