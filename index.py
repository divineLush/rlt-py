import Models as M
import State as S

# TODO: find most occupied trailer tuple

state = S.State()
prev = state.totalWaitingTime()
print(prev)
for i in range(1000):
    state.randSwap()
    print(state.totalWaitingTime())
print(prev, state.totalWaitingTime())
