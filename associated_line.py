# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 01:44:56 2018

@author: Etcyl
"""
import set_class

class line():
    """A line is a group of associated sets"""
    #The association specifies the number of set_classes() in the line
    
    type = 'Associative'
    
    def __init__(self, association):
        self.num_sets = association
        self.set = [0]*association
        for i in range(association):
            self.set[i] = set_class.set()

    def setStatusBit(self, index):
        self.set[index].setStatusBit()
    
    def clearStatusBit(self, index):
        self.set[index].clearStatusBit()
        
    def getStatusBit(self, index):
        return self.set[index].getStatusBit()
            
    def setValidBit(self, index):
        self.set[index].setValidBit()
    
    def clearValidBit(self, index):
        self.set[index].clearValidBit()
    
    def getValidBit(self, index):
        return self.set[index].getValidBit()
    
    def setDirtyBit(self, index):
        self.set[index].setDirtyBit()
        
    def getDirtyBit(self, index):
        return self.set[index].getDirtyBit()
        
    def clearDirtyBit(self, index):
        self.set[index].clearDirtyBit()
        
    def writeTagBits(self, index, tag_bits):
        self.set[index].writeTagBits(tag_bits)
        
    def getTagBits(self, index):
        return self.set[index].getTagBits()

    def getDataBits(self, index):
        return self.set[index].getDataBits()
    
    def setDataBits(self, index, data):
        self.set[index].setDataBits(data)
