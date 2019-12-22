
from random import choice

days = list(range(1,31))
dummy_vals = [0,0,25,30,45,60,75]
workouts = [choice(dummy_vals) for _ in range(30)]

from matplotlib import pyplot as plt

plt.bar(days, workouts)
plt.xticks(days)
plt.ylabel("minutes")
plt.xlabel("day of month")
plt.title("workout minutes per day")
plt.show()
