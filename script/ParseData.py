#! /usr/bin/env python3

import sys

class UData:
    def __init__(self):
        self.__fname = ""
        self.__data = []

    def add(self, array):
        self.__data.append(array)
        self.sort()

    def printAll(self):
        for cl in self.__data:
            print('{:04x}, {:04x}, '.format(cl[0], cl[1]) + ", ".join(cl[2:]))

    def merge(self, uobj):
        cdata = self.__data
        udata = uobj.GetData()
        udata.sort(key = lambda x: x[0])
        self.__data = []
        cid = 0
        uid = 0
        while (cid < len(cdata)) and (uid < len(udata)):
            while udata[uid][1] < cdata[cid][0]:
                uid += 1
            if cdata[cid][0] == cdata[cid][1]:
                carr = cdata[cid]
                carr += udata[uid][2:]
                self.add(carr)
                cid += 1
                continue
            cst = cdata[cid][0]
            while udata[uid][1] < cdata[cid][1]:
                carr = [cst, udata[uid][1]]
                cst = udata[uid][1] + 1
                carr += cdata[cid][2:]
                carr += udata[uid][2:]
                self.add(carr)
                uid += 1
            carr = [cst]
            carr += cdata[cid][1:]
            carr += udata[uid][2:]
            self.add(carr)
            cid += 1

    def len(self):
        return len(self.__data)

    def GetData(self):
        return self.__data

    def sort(self):
        self.__data.sort(key = lambda x: x[0])

    def load(self, fname):
        self.__fname = fname
        with open(self.__fname) as f:
            for sl in f:
                sl = sl.strip()
                if (len(sl) > 0) and (sl[0] != "#"):
                    slc = sl.find('#')
                    if slc > 0:
                        sl = sl[0:slc]
                    sla = sl.split(';')
                    sla = list(map(lambda x: x.strip(), sla))
                    sln = sla[0].split('..')
                    if len(sln) == 1:
                        sln += sla
                    else:
                        sln += sla[1:]
                    sln[0] = int(sln[0], 16)
                    sln[1] = int(sln[1], 16)
                    self.add(sln)



if __name__ == "__main__":
    if len(sys.argv) > 2:
        cobj = UData()
        cobj.load(sys.argv[1])
        dobj = UData()
        dobj.load(sys.argv[2])
        cobj.merge(dobj)
        cobj.printAll()


