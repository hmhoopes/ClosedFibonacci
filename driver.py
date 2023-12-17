import fib_finder
import time
import matplotlib.pyplot as plt
import numpy as np
max = 10000
rec_times = [0 for i in range(max)]
iter_times = [0 for i in range(max)]
x = range(max)
for i in range(max):
    print(f"for index = {i}:")

    '''start = time.time()
    rec_val = fib_finder.rec_finder(i)
    end = time.time()
    rec_time = end - start'''

    start = time.time()
    iter_val = fib_finder.iterative_finder(i)
    end = time.time()
    iter_time = end - start

    #rec_times[i] = rec_time
    iter_times[i] = iter_time
    #print(f"\trec val: {rec_val}, elapsed time: {rec_time} \n\titer. val: {iter_val}, elapsed time: {iter_time}")

'''
plt.plot(x, rec_times, label="rec. times")
plt.plot(x, iter_times, label="iter. times")
plt.legend()
plt.show()
'''
plt.plot(x, iter_times, label="iter. times")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, iter_times, 1))(np.unique(x)), label="line of best fit")
plt.legend()
plt.show()