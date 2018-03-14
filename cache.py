# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:46:24 2018
Matt Fleetwood
ECE 485
Winter 2018
Cache class for simulating a single level (L1) of cache.
Cache with configurable set size, cache line size, and associativity.
Associativity ranging between 1 and 8.
Cache line size ranging between 32 bytes and 128 bytes.
"""

import associated_line as a_line
import math

class cache():
    """A cache is a small, fast, expensive block of memory"""
    #The cache responds to memory accesses and calculates statistics of requests
    
    type = 'L1 Cache with 1-bit LRU replacement policy'
    
    def __init__(self, num_sets, associativity, line_size):
        self.num_sets = num_sets
        self.reads = 0
        self.writes = 0
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.writebacks = 0
        self.hit_ratio = 0
        self.miss_ratio = 0
        self.total_accesses = 0
        self.line_size = line_size
        self.cache_tag = 32 - int(math.log(num_sets*line_size, 2))
        self.index = int(32 - (self.cache_tag + int(math.log(self.line_size, 2))))
        self.sets = [0]*num_sets
        print('Number of sets are:', num_sets, '\nAssociativity is:', associativity, '\nLine size is:', line_size)
        
        if 1 > associativity or associativity > 8:
            while 1 > associativity or associativity > 8:
                associativity = int(input('Associativity can only be between 1 and 8, please enter the associativity: '))
        
        self.associativity = associativity   
        
        if 32 > line_size or line_size > 128:
            while 32 > line_size or line_size > 128:
                line_size = int(input('Line size can only be between 32 and 128, please enter the line size: '))        

        self.line_size = line_size
        
    def updateReads(self):
        self.reads += 1
    
    def getReads(self):
        return self.reads
    
    def updateWrites(self):
        self.writes +=1
        
    def getWrites(self):
        return self.writes
        
    def updateHits(self):
        self.hits += 1
        
    def getHits(self):
        return self.hits
        
    def updateMisses(self):
        self.misses += 1
        
    def getMisses(self):
        return self.misses
        
    def updateEvictions(self):
        self.evictions += 1
        
    def getEvictions(self):
        return self.evictions
        
    def updateWritebacks(self):
        self.writebacks += 1
        
    def getWritebacks(self):
        return self.writebacks
        
    def updateTotalAccesses(self):
        self.total_accesses += 1
    
    def getTotalAccesses(self):
        return self.total_accesses
        
    def updateHitRatio(self):
        if(self.hits == 0):
            self.hit_ratio = 0
        elif(self.total_accesses == 0):
            print('NUM_ACCESS_ERROR: self reference to total accesses is 0 making the H.R. undefined; setting H.R. to 0.')
            self.hit_ratio = 0
        else:
            self.hit_ratio = (self.hits / self.total_accesses)*100
    
    def getHitRatio(self):
        return self.hit_ratio
            
    def updateMissRatio(self):
        if(self.misses == 0):
            self.miss_ratio = 0
        elif(self.total_accesses == 0):
            print('NUM_ACCESS_ERROR: self reference to total accesses is 0 making the M.R. undefined; setting M.R. to 0.')
            self.miss_ratio = 0
        else:
            self.miss_ratio = (self.misses / self.total_accesses)*100
        
    def getMissRatio(self):
        return self.miss_ratio
    
    def updateStatistics(self):
        self.updateHitRatio()
        self.updateMissRatio()
        
    def printStatistics(self):
        self.updateStatistics()
        print('Total number of cache accessess: ', self.total_accesses)
        print('Number of cache reads: ', self.reads)   
        print('Number of cache writes: ', self.writes)        
        print('Number of cache hits: ', self.hits)
        print('Number of cache misses: ', self.misses)
        print('Cache hit ratio: ', self.hit_ratio, '%') 
        print('Cache miss ratio: ', self.miss_ratio, '%') 
        print('Number of evictions: ', self.evictions)
        print('Number of writebacks: ', self.writebacks)
        
    def build(self):
        for i in range(self.num_sets):
            self.sets[i] = a_line.line(self.associativity)
        
    def serveAccess(self, access_type, mem_address):
        self.total_accesses += 1
        #address = format(mem_address, 'x')
        M = int(math.log(self.line_size, 2)) #Number of byte select bits (lowest-order bits)
        O = int(math.log(self.num_sets, 2))  #Number of set index bits (immediately after M bits, and before the cache tag bits, N)
        to_shift = int(mem_address) >> (M + O) #Tag bits
        tags = to_shift << (M + O)  #Cache tags
        set_index = mem_address - tags
        set_index = set_index >> M   
        #Check if the access is a read
        if access_type == 0:
            self.updateReads()
            for i in range(self.associativity):
                if(self.sets[set_index].getValidBit(i) == 1):
                    if(self.sets[set_index].getTagBits(i) == to_shift):
                        self.updateHits()
                        self.sets[set_index].setStatusBit(i)
                        return
                elif(self.sets[set_index].getValidBit(i) == 0):
                    self.updateMisses()
                    self.sets[set_index].writeTagBits(i, to_shift)
                    self.sets[set_index].setStatusBit(i)
                    self.sets[set_index].setValidBit(i)
                    return
            self.updateMisses()
            self.updateEvictions()
            MRU_bits = 0
            eviction_candidate = 0
            for i in range(self.associativity):
                if(self.sets[set_index].getStatusBit(i) == 1):
                    MRU_bits = MRU_bits + 1
                elif(self.sets[set_index].getStatusBit(i) == 0):
                    eviction_candidate = i
                    break
            if(MRU_bits == self.associativity):
                eviction_candidate = 0
                for i in range(self.associativity):
                    self.sets[set_index].clearStatusBit(i)
            if(self.sets[set_index].getDirtyBit(eviction_candidate) == 1):
                self.updateWritebacks()
            self.sets[set_index].writeTagBits(eviction_candidate, to_shift)
            self.sets[set_index].setStatusBit(eviction_candidate)
            self.sets[set_index].setValidBit(eviction_candidate)
        else:
            self.updateWrites()
            for i in range(self.associativity):
                if(self.sets[set_index].getValidBit(i) == 0):
                    self.updateMisses()
                    self.sets[set_index].setValidBit(i)
                    self.sets[set_index].setStatusBit(i)
                    self.sets[set_index].writeTagBits(i, to_shift)
                    self.sets[set_index].setDirtyBit(i)
                    return
                elif(self.sets[set_index].getValidBit(i) == 1):
                    if(self.sets[set_index].getTagBits(i) == to_shift):
                        self.updateHits()
                        self.sets[set_index].setStatusBit(i)
                        self.sets[set_index].setDirtyBit(i)
                        return
            self.updateMisses()
            self.updateEvictions()
            MRU_bits = 0
            eviction_candidate = 0
            for i in range(self.associativity):
                if(self.sets[set_index].getStatusBit(i) == 1):
                    MRU_bits += 1
                elif(self.sets[set_index].getStatusBit(i) == 0):
                    eviction_candidate = i
                    break
            if(MRU_bits == self.associativity):
                eviction_candidate = 0
                for i in range(self.associativity):
                    self.sets[set_index].clearStatusBit(i)
            if(self.sets[set_index].getDirtyBit(eviction_candidate) == 1):
                self.updateWritebacks()
            self.sets[set_index].writeTagBits(eviction_candidate, to_shift)
            self.sets[set_index].setStatusBit(eviction_candidate)
            self.sets[set_index].setValidBit(eviction_candidate)
            self.sets[set_index].setDirtyBit(eviction_candidate)
            return      
