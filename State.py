import Models as M
import random

# arrivalTimeDiff = 2

class State:
    def __init__(self, trailersNum = random.randint(10, 50)):
        self.trailers = [M.Trailer(random.randint(0, 24), i) for i in range(trailersNum)]
        self.warehouse = M.Warehouse()
        self.trailers.sort(key=lambda trailer: trailer.arrivalTime)
        # self.assignTrailersRandomly() if isRandom else self.assignTrailers()

    def assignTrailers(self):
        for loc in self.warehouse.locations:
            loc.assignedTrailers = []
        for trailer in self.trailers:
            self.assignTrailerToLoc(trailer, self.warehouse.leastOccupiedLoc())

    def assignTrailersRandomly(self):
        for loc in self.warehouse.locations:
            loc.assignedTrailers = []
        for trailer in self.trailers:
            self.assignTrailerToLoc(trailer, self.warehouse.randomLoc())

    def assignTrailersToLocsByNums(self, locNums):
        for i in range(len(self.trailers)):
            loc = self.warehouse.locations[locNums[i]]
            self.assignTrailerToLoc(self.trailers[i], loc)

    def assignTrailerToLoc(self, trailer, loc):
        trailer.assignedLocNum = loc.num
        trailer.setWaitingTimeByLoc(loc)
        loc.assignTrailer(trailer)

    def mostWaitingTuple(self):
        waitingTimes = [trailer.waitingTime for trailer in self.trailers]
        maxVal = waitingTimes[0]
        maxIndex = 0
        for i in range(len(waitingTimes)):
            if waitingTimes[i] > maxVal:
                maxVal = waitingTimes[i]
                maxIndex = i
        return self.makeTrailerTuple(maxIndex, self.randTrailerIndex())

    def randTrailerIndex(self):
        return random.randint(0, len(self.trailers)-1)

    def randSwap(self):
        self.swapTrailers(self.makeTrailerTuple(self.randTrailerIndex(), self.randTrailerIndex()))

    def swapMostWaitingTrailer(self):
        self.swapTrailers(self.mostWaitingTuple())

    def swapTrailers(self, randTrailers):
        '''
            takes tuple of trailers and swaps if its reasonable
            if target function gets worse it swaps
        '''
        # curArrivalDiff = abs(randTrailers[0].arrivalTime - randTrailers[1].arrivalTime)
        # if curArrivalDiff < arrivalTimeDiff: # if swap is reasonable
        if randTrailers[1].arrivalTime < randTrailers[0].arrivalTime:
            # sort by arrival time
            randTrailers[1], randTrailers[0] = randTrailers[0], randTrailers[1]
        # swap trailers in locs
        locs = [self.getLocByTrailer(randTrailers[i]) for i in range(2)]
        isValid = lambda any: any != -1
        isTupleValid = lambda tuple: isValid(tuple[0]) and isValid(tuple[1])
        if (isTupleValid(locs)):
            # find trailers and swap
            trIndexes = [self.getTrailerIndexByItsNum(tr) for tr in randTrailers]
            if (isTupleValid(trIndexes)):
                prevTime = self.totalWaitingTime()
                self.swapTrailersByIndexes(trIndexes[0], trIndexes[1])
                if prevTime < self.totalWaitingTime(): # if it gets worse
                    self.swapTrailersByIndexes(trIndexes[0], trIndexes[1])

    def makeTrailerTuple(self, i, j):
        return [self.trailers[i], self.trailers[j]]

    def getLocByTrailer(self, trailer):
        res = -1
        for loc in self.warehouse.locations:
            if loc.getTrailerIndexByItsNum(trailer.num) != -1:
                res = loc
        return res

    def swapTrailersByIndexes(self, i, j):
        self.trailers[i], self.trailers[j] = self.trailers[j], self.trailers[i]
        self.assignTrailers()

    def getTrailerIndexByItsNum(self, trailer):
        res = -1
        trailers = self.trailers
        for i in range(len(trailers)):
            if trailers[i].num == trailer.num:
                res = i
                break
        return res

    def totalWaitingTime(self):
        res = 0
        for trailer in self.trailers:
            res += trailer.waitingTime
        return res

    def localSearch(self, n = 10000):
        prev = self.totalWaitingTime()
        for i in range(n):
            z = random.randint(0, 2)
            if z == 1:
                self.swapMostWaitingTrailer()
            else :
                self.randSwap()
        print(prev, self.totalWaitingTime())
