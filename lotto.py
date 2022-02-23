import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

x = {}
nums = []

f = open('lotto.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    x.update({line[0]: line[1:len(line)]})
    for num in range(1, len(line)):
        nums.append(line[num])

f.close()

index = pd.Index(nums)
df = pd.DataFrame(x)

print(df)

rng = np.random.default_rng(seed=42)
first = [9, 13, 21, 25, 32, 42]
first.sort()
second = [10, 23, 29, 33, 37, 40]
second.sort()
xarr = np.array([first, second])

print(np.var(xarr, axis=1))
print(np.corrcoef(xarr))
num_array = []
count = 0

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(xarr[0], xarr[1])
plt.show()

values = []

plot_x = []
for i in range(1, 46):
    plot_x.append(i)

# while count < 1000:
#     count += 1
#     num_array.append(int(46*random.random()))

# a = np.array(num_array)


# for n in range(1, 46):
#     values.append((x == n).sum())

# print(values)
# numbers = pd.DataFrame(index.value_counts())
# print(numbers.loc[:, [0]])
# b = []
# for i in numbers:
#     b.append(i)
# plt.bar(plot_x, b)
# plt.xticks(plot_x, plot_x)
# plt.show()
