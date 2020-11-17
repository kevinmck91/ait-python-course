import matplotlib.pyplot as plt
import datetime

data_by_state = {}

with open("amazon2.csv") as datafile:

    for line in datafile:

        year, state, month, fires, date = line.strip().split(",")

        if not state in data_by_state:
            data_by_state[state] = int(fires)

        else:
            data_by_state[state] += int(fires)

# To start, create an instance of Figure and an instance of Axes:
# The Figure is like a canvas, and the Axes is a part of that canvas on which we will make a particular
# visualization
fig, ax = plt.subplots()

ax.set_title("Fires in Acre State, Brazil 1998-2017")

y_pos = [i for i in range(len(data_by_state))]

# Set the y tick labels
ax.set_yticks(y_pos)
ax.set_yticklabels(data_by_state.keys())

# Set the labels on the axis
ax.set_ylabel("State")
ax.set_xlabel("Total number of fires")

ax.barh(y_pos, data_by_state.values(), align="center")
plt.show()

fig.savefig("amazon_bar_chart.png", bbox_inches='tight')

# In general, the code to create a horizontal bar chart is:
# ax.barh(list_of_positions, list_of_values)