from matplotlib import pyplot
import matplotlib 
import numpy
from textwrap import wrap
import matplotlib.ticker as plt

with open('settings.txt', 'r') as file:
    settings=[float(i) for i in file.read().split('\n')]

data=numpy.loadtxt('data.txt', dtype=int) * settings[1]
data_time=numpy.array([i*settings[0] for i in range(data.size)])
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

ax.axis([data_time.min(), data_time.max()+1, data.min(), data.max()+0.2])

ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))

ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепочке', 60)), loc = 'center')

ax.grid(which='major', color = 'green')
ax.minorticks_on()
ax.grid(which='minor', color = 'green', linestyle = ':')

ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

ax.plot(data_time, data, c='black', linewidth=1, label = 'V(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'red', s=10)
ax.text(6, 2.25, "Время Зарядки! ~ 5.1 c", fontsize=40)
ax.text(6, 1.75, "Время Разрядки! ~ 6.9 c", fontsize=40)


ax.legend(shadow = False, loc = 'right', fontsize = 30)

fig.savefig('graph.svg')
