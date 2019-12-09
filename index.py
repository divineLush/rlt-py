import Models as M
import State as S

state = S.State()
state.assignTrailers()
print(state.totalOccupationTime())
state.randSwap()
print(state.totalOccupationTime())
