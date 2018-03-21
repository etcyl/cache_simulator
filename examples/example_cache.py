# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 06:35:03 2018

@author: Etcyl
"""
import cache

theFile = open("trace1.txt", "rb")
theInts = []

for val in theFile.read().split():
    theInts.append(val)
theFile.close()

traces = []
for i in range(len(theInts)):
    traces.append(int(float.fromhex(theInts[i].decode())))

b = cache.cache(64, 1, 64)
b.build()

count = 0
stop = int(len(traces) / 2)
for i in range(stop):
    b.serveAccess(traces[count], traces[count + 1])
    count = count + 2
print("1 way, 32B lines; number of sets ranging from 64, 128, 256, and 512")
b.printStatistics()
d_ratio = b.writebacks / b.evictions
print("Dirty ratio is: ", d_ratio)
#4KB / 64B --> 2^12 / 2^6 = 2^6 --> 64 sets
#8KB / 64B --> 2^13 / 2^6 = 2^7 --> 128 sets
#16KB / 64B --> 2^14 / 2^6 = 2^8 --> 256 sets
#32KB / 64B --> 2^15 / 2^6 = 2^9 --> 512 sets

print("End of 64 sets\n")

b1 = cache.cache(128, 1, 64)
b1.build()

count = 0
stop = int(len(traces) / 2)
for i in range(stop):
    b1.serveAccess(traces[count], traces[count + 1])
    count = count + 2

b1.printStatistics()
d_ratio = b1.writebacks / b1.evictions
print("Dirty ratio is: ", d_ratio)
print("End of 128 sets\n")

b2 = cache.cache(256, 1, 64)
b2.build()

count = 0
stop = int(len(traces) / 2)
for i in range(stop):
    b2.serveAccess(traces[count], traces[count + 1])
    count = count + 2

b2.printStatistics()
d_ratio = b2.writebacks / b2.evictions
print("Dirty ratio is: ", d_ratio)
print("End of 256 sets\n")


b3 = cache.cache(512, 1, 64)
b3.build()

count = 0
stop = int(len(traces) / 2)
for i in range(stop):
    b3.serveAccess(traces[count], traces[count + 1])
    count = count + 2

b3.printStatistics()
d_ratio = b3.writebacks / b3.evictions
print("Dirty ratio is: ", d_ratio)
