import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10, 6))

point_numbers = range(rw.num_points)

ax.scatter(
    rw.x_values,
    rw.y_values,
    c=point_numbers,
    cmap=plt.cm.Blues,
    s=1
)

ax.set_title("Random Walk Simulation")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")

plt.show()