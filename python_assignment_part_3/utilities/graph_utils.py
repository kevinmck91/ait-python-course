import matplotlib.pyplot as plt


def generate_pie_chart(catagories_list: list, figures_list: list, name):

    dict = {}

    for key, value in zip(catagories_list, figures_list):

        if key in dict:
            current_value = dict[key]
            accumulative_value = current_value + value
            dict[key] = accumulative_value
        else:
            dict[key] = value

    fig, ax = plt.subplots()

    ax.set_title(name)

    ax.pie(dict.values(), labels=dict.keys(), autopct="%.0f%%")

    plt.show()




def generate_barchart_single(my_list: str):

    dict = {}

    for value in my_list:

        if not value in dict:
            dict[value] = 1
        else:
            dict[value] += 1

    fig, ax = plt.subplots()

    y_pos = [i for i in range(len(dict))]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dict.keys())

    ax.set_ylabel("")
    ax.set_xlabel("")

    ax.barh(y_pos, dict.values(), align="center")
    plt.show()