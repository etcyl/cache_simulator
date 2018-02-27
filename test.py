# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 06:35:03 2018

@author: Etcyl
"""
import cache

theFile = open("test.txt", "rb")
theInts = []
for val in theFile.read().split():
    theInts.append(val)
theFile.close()

traces = []
for i in range(len(theInts)):
    traces.append(int(float.fromhex(theInts[i].decode())))

b = cache.cache(10, 4, 64)
b.build()
b.serveAccess(0, 0x0F7A53C20)

b.serveAccess(0, 0x111153C20)

b.serveAccess(0, 0x222253C20)

b.serveAccess(0, 0x444453C20)

b.serveAccess(0, 0x555553C20)

b.serveAccess(0, 0x763253C20)

b.serveAccess(0, 0x092453C20)

b.serveAccess(0, 0x195853C20)

b.serveAccess(1, 0x0F7A53C20)

b.serveAccess(1, 0x111153C20)

b.serveAccess(1, 0x222253C20)

b.serveAccess(1, 0x444453C20)

b.serveAccess(1, 0x555553C20)

b.serveAccess(1, 0x763253C20)

b.serveAccess(1, 0x092453C20)

b.serveAccess(1, 0x195853C20)

b.printStatistics()

#y = theInts[X].decode()
#addy = int(float.from(y))
