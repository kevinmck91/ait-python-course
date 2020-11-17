import matplotlib.pyplot as plt

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

ax.pie(data_by_state.values(), labels=data_by_state.keys())
plt.show()

fig.savefig("amazon_pie_chart.png", bbox_inches='tight')