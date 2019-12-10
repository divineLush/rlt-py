import random

class Trailer:
    def __init__(self, arrivalTime, num):
        self.palettes = [Palette() for i in range(random.randint(2, 15))]
        self.arrivalTime = arrivalTime
        self.assignedGateNum = 0
        self.waitingTime = 0
        self.num = num

    def totalWeight(self):
        res = 0
        for palette in self.palettes:
            res += palette.weight
        return res

    def serviceTime(self):
        return self.totalWeight()*2


class Palette:
    def __init__(self):
        self.weight = random.randint(100, 600)


class Gate:
    def __init__(self, assignedTrailerNum):
        self.assignedTrailerNum = assignedTrailerNum
        self.totalOccupationTime = 0


class Location:
    def __init__(self, gate, num):
        self.capacity = random.randint(5000, 10000)
        self.storedWeight = 0
        self.gate = gate
        self.num = num


class Warehouse:
    def __init__(self):
        self.locations = [Location(Gate(0), i) for i in range(6)]

    def leastOccupiedLoc(self):
        minLoc = self.locations[0]
        for l in self.locations:
            if l.gate.totalOccupationTime < minLoc.gate.totalOccupationTime:
                minLoc = l
        return minLoc
