import matplotlib.pyplot as plt


def generate_pie_chart_single(my_list: str):

    dict = {}

    for value in my_list:

        if not value in dict:
            dict[value] = 1
        else:
            dict[value] += 1

    fig, ax = plt.subplots()

    ax.set_title("Pie chart generated from list : ")

    ax.pie(dict.values(), labels =dict.keys())
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