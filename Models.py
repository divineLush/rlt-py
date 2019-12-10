import random

class Trailer:
    def __init__(self, arrivalTime, num):
        self.palettes = [Palette() for i in range(random.randint(2, 15))]
        self.arrivalTime = arrivalTime
        self.assignedLocNum = 0
        self.waitingTime = 0
        self.num = num

    def setWaitingTimeByLoc(self, loc):
        self.waitingTime = loc.totalOccupationTime() - self.arrivalTime

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

class Location:
    def __init__(self, num):
        self.capacity = random.randint(5000, 10000)
        self.assignedTrailers = []
        self.num = num

    def totalOccupationTime(self):
        res = 0
        for trailer in self.assignedTrailers:
            res += trailer.serviceTime()
        return res

    def getTrailerIndexByItsNum(self, num):
        res = -1
        for i in range(len(self.assignedTrailers)):
            if self.assignedTrailers[i].num == num:
                res = i
                break
        return res


class Warehouse:
    def __init__(self):
        self.locations = [Location(i) for i in range(6)]

    def leastOccupiedLoc(self):
        minLoc = self.locations[0]
        for l in self.locations:
            if l.totalOccupationTime() < minLoc.totalOccupationTime():
                minLoc = l
        return minLoc
