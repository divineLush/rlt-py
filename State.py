import Models as Models
import random

class State:
    def __init__(self):
        trailersNum = random.randint(10, 50)
        self.trailers = [Models.Trailer(random.randint(0, 24)) for i in range(trailersNum)]
        self.warehouse = Models.Warehouse()

    def assignTrailers(self):
        for i in range(len(self.trailers)):
            trailer = self.trailers[i]
            minLoc = self.warehouse.leastOccupiedLoc()
            minLoc.gate.assignedTrailerNum = i
            minLoc.gate.totalOccupationTime += trailer.serviceTime()
            # TODO: fix error
            # minloc.storedWeight += trailer.totalWeight()
            # assignedLocNum
            trailer.assignedGateNum = minLoc.num
            trailer.wasServiced = True

    def randSwap(self):
        foo1 = self.trailers[random.randint(0, len(self.trailers))]
        foo2 = self.trailers[random.randint(0, len(self.trailers))]
        prevTime = self.totalOccupationTime()
        foo1, foo2 = foo2, foo1
        self.assignTrailers()
        if prevTime > self.totalOccupationTime():
            foo1, foo2 = foo2, foo1

    def totalOccupationTime(self):
        res = 0
        for loc in self.warehouse.locations:
            res += loc.gate.totalOccupationTime
        return res
