import matplotlib.pyplot as plt
import matplotlib.markers as mak

circle1 = plt.Circle((0, 0), 0.1,facecolor="none",edgecolor='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
circle3 = plt.Circle((1, 1), 0.01, facecolor="none",edgecolor='r')

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

ax.set_xlim((0, 10))
ax.set_ylim((0, 10))
plt.show()
fig.savefig('plotcircles.png')