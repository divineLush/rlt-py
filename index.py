import Models as M
import State as S

state = S.State()
print(state.totalWaitingTime())
state.assignTrailers()
print(state.totalWaitingTime())
for i in range(100):
    state.randSwap()
print(state.totalWaitingTime())
