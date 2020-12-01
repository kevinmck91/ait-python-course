import matplotlib.pyplot as plt


def generate_pie_chart(categories_list: list, figures_list: list, name="Pie Chart"):
    """
        This function is designed to take in two lists and generate a Pie Chart

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category

        Returns
        -------
        No Return Type - A graph is saved to the filesystem

    """

    dict = {}

    for key, value in zip(categories_list, figures_list):

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




def generate_barchart(categories_list: list, figures_list: list, name="Bar Chart", label_x="Values" ,label_y="Categories"):
    """
        This function is designed to take in two lists and generate a Bar Chart

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category

        Returns
        -------
        No Return Type - A graph is saved to the filesystem

    """

    dict = {}

    for key, value in zip(categories_list, figures_list):

        if key in dict:

            if key == "TotalUS":
                continue

            current_value = dict[key]
            accumulative_value = current_value + value
            dict[key] = accumulative_value
        else:
            if key == "TotalUS":
                continue
            dict[key] = value

    fig, ax = plt.subplots()

    y_pos = [i for i in range(len(dict))]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dict.keys())

    ax.set_title(name)
    ax.set_ylabel(label_y)
    ax.set_xlabel(label_x)

    ax.barh(y_pos, dict.values(), align="center")
    ax.ticklabel_format(axis='x', style='sci', scilimits=(5, 15))

    plt.show()


