import matplotlib.pyplot as plt

data_by_state = {}

# We can use a Dictionary and plot the keys vs value
fires = [1,2,3,4,5,6,77,78,99,77,5,4]
months = ["m1","m2","m3","m4","m5","m6","m7","m8","m9","m10","m11","m12",]

# To start, create an instance of Figure and an instance of Axes:
# The Figure is like a canvas, and the Axes is a part of that canvas on which we will make a particular
# visualization
fig, ax = plt.subplots()

ax.set_title("Fires in Acre State, Brazil 1998-2017")

y_pos = [i for i in range(len(data_by_state))]


# Set the labels on the axis
ax.set_ylabel("fires")
ax.set_xlabel("months")

ax.plot(months, fires)
plt.show()

fig.savefig("amazon_line_plot.png", bbox_inches='tight')

# In general, the code to create a horizontal bar chart is:
# ax.barh(list_of_positions, list_of_values)