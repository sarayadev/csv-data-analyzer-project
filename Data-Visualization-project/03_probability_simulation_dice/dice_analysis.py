import matplotlib.pyplot as plt
from dice import Dice

dice = Dice()

results = []
for _ in range(1000):
    results.append(dice.roll())

frequencies = []
for value in range(1, dice.sides + 1):
    frequencies.append(results.count(value))

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.bar(range(1, dice.sides + 1), frequencies)

ax.set_title("Dice Roll Frequency Distribution")
ax.set_xlabel("Die Face Value")
ax.set_ylabel("Frequency")

plt.show()