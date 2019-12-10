import Models as Models
import random

class State:
    def __init__(self):
        trailersNum = random.randint(10, 50)
        self.trailers = [Models.Trailer(random.randint(0, 24), i) for i in range(trailersNum)]
        self.warehouse = Models.Warehouse()

    def assignTrailers(self):
        for trailer in self.trailers:
            minLoc = self.warehouse.leastOccupiedLoc()
            self.assignTrailerToLoc(trailer, minLoc)

    def assignTrailerToLoc(self, trailer, loc):
        trailer.assignedGateNum = loc.num
        trailer.waitingTime = loc.gate.totalOccupationTime - trailer.arrivalTime
        loc.gate.totalOccupationTime += trailer.serviceTime()
        loc.gate.assignedTrailerNum = trailer.num

    def randSwap(self):
        prevTime = self.totalWaitingTime()
        t1 = self.trailers[random.randint(0, len(self.trailers) - 1)]
        t2 = self.trailers[random.randint(0, len(self.trailers) - 1)]
        loc1 = self.warehouse.locations[t1.assignedGateNum]
        loc2 = self.warehouse.locations[t2.assignedGateNum]
        self.assignTrailerToLoc(t1, loc2)
        self.assignTrailerToLoc(t2, loc1)
        if prevTime < self.totalWaitingTime():
            self.assignTrailerToLoc(t1, loc1)
            self.assignTrailerToLoc(t2, loc2)

    def totalOccupationTime(self):
        res = 0
        for loc in self.warehouse.locations:
            res += loc.gate.totalOccupationTime
        return res

    def totalWaitingTime(self):
        res = 0
        for trailer in self.trailers:
            res += trailer.waitingTime
        return res
