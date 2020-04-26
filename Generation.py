import State as S
import random


class Generation:
    def __init__(self, solNum = random.randint(10, 100), trailersNum = random.randint(50, 200)):
        init_state = S.State(trailersNum)
        self.generation = [init_state for i in range(solNum)]
        randLocNums = [random.randint(0,5) for i in range(trailersNum * solNum)]
        for i in range(len(self.generation)):
            self.generation[i].assignTrailersToLocsByNums(randLocNums[i : i + trailersNum])
        for state in self.generation:
            print(state.totalWaitingTime())
        print()
        print()
