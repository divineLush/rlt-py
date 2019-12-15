import Models as M
import State as S
import random

# TODO: find most occupied trailer tuple

# def gr(target_f_log):
#     x = np.arange(len(target_f_log))
#     plt.plot(x, target_f_log)
#     plt.xlabel(r'$step$')
#     plt.ylabel(r'$value$')
#     plt.title(r'$Target Function$')
#     plt.grid(True)
#     plt.show()


state = S.State()
prev = state.totalWaitingTime()
t_f_log = []
for i in range(1000):
    z = random.randint(0, 2)
    if z == 1:
        state.swapMostWaitingTrailer()
    else :
        state.randSwap()
    t_f_log.append(self.totalWaitingTime())

# gr(t_f_log)