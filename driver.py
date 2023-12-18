import fib_finder
import time
import matplotlib.pyplot as plt
import numpy as np

max = 20000
closed_times = [0 for i in range(max)]
iter_times = [0 for i in range(max)]
inaccuracy = [0 for i in range(max)]
x = range(max)
for i in range(max):
    print(f"for index = {i}:")

    start = time.time()
    closed_val = fib_finder.closed_form(i)
    end = time.time()
    closed_time = end - start

    start = time.time()
    iter_val = fib_finder.iterative_finder(i)
    end = time.time()
    iter_time = end - start

    closed_times[i] = closed_time
    iter_times[i] = iter_time
    inaccuracy[i] = abs(iter_time - closed_time)
    #print(f"\trec val: {rec_val}, elapsed time: {rec_time} \n\titer. val: {iter_val}, elapsed time: {iter_time}")

plt.plot(x, iter_times, label="iter. times")
plt.plot(x, closed_times, label="closed times")
plt.legend()
plt.show()

plt.plot(x, inaccuracy, label="inaccuracy")
plt.legend()
plt.show()