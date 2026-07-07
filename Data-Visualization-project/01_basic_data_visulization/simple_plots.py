import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.plot(x_values, y_values, linewidth=2)

ax.set_title("Square Number Relationship")
ax.set_xlabel("Input Value")
ax.set_ylabel("Squared Output")

plt.show()