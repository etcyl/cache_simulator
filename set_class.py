# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:45:35 2018

@author: Etcyl
"""

class set():
    """A set is a line or block in a cache memory"""
    #The set stores a valid bit, tag and data bits.
    
    type ='Set of an associative cache'
    
    def __init__(self):
        self.valid_bit = 0
        self.tag_bits = 0
        self.data_bits = 0
        self.dirty_bit = 0
        self.status_bit = 0

    def setStatusBit(self):
        self.status_bit = 1
    
    def clearStatusBit(self):
        self.status_bit = 0
        
    def getStatusBit(self):
        return self.status_bit
     
    def setValidBit(self):
        self.valid_bit = 1
    
    def clearValidBit(self):
        self.valid_bit = 0
        
    def toggleValidBit(self):
        if(self.valid_bit == 1):
            self.valid_bit = 0
        else:
            self.vlaid_bit = 1
    
    def getValidBit(self):
        return self.valid_bit
    
    def setDirtyBit(self):
        self.dirty_bit = 1
        
    def getDirtyBit(self):
        return self.dirty_bit
        
    def clearDirtyBit(self):
        self.dirty_bit = 0
        
    def writeTagBits(self, tag_bits):
        self.tag_bits = tag_bits
        
    def getTagBits(self):
        return self.tag_bits

    def getDataBits(self):
        return self.data_bits

    def setDataBits(self, data):
        self.data_bits = data
