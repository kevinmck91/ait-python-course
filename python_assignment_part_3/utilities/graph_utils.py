import matplotlib.pyplot as plt


def generate_category_figure_pie_chart(categories_list: list, figures_list: list, name="Pie Chart"):
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




def generate_category_figure_barchart(categories_list: list, figures_list: list, name="Bar Chart", label_x="Values" ,label_y="Categories"):
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

def generate_basic_boxplot(list_of_figures, y_axis_name, x_axis_name):
    fig, ax = plt.subplots()

    ax.boxplot(list_of_figures, showfliers=False)

    ax.set_title("Boxplot")
    ax.set_ylabel(y_axis_name)
    ax.set_xlabel(x_axis_name)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(5, 15))
    plt.show()

def generate_category_figure_boxplot(categories_list, figures_list, category_name, figures_name, name="Box Plot"):
    """
        This function takes in a list of values, a list of figures and a parameter

        Parameters
        ----------
        list of figures - The values that will be repersented on the box plot
        list of categories - a list of categories, once category will be chosen to narrow down the list of values
        category_name

        Returns
        -------
        No Return Type - A graph is saved to the file system

    """

    list_of_figures = [value for key, value in zip(categories_list, figures_list) if key == category_name]

    generate_basic_boxplot(list_of_figures, figures_name, category_name)


