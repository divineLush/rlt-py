import Models as M
import State as S
import random

# TODO: find most occupied trailer tuple

state = S.State()
prev = state.totalWaitingTime()
for i in range(10000):
    z = random.randint(0, 2)
    if z == 1:
        state.swapMostWaitingTrailer()
    else :
        state.randSwap()
print(prev, state.totalWaitingTime())
