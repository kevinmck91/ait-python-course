import matplotlib.pyplot as plt
import datetime
from python_assignment_part_3.utilities import data_structure_utils



def generate_date_line_chart(date_list: list, figures_list: list, name, x_label="", y_label=""):
    """
        This function is designed to take in two lists and generate a line graph

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - A graph is saved to the filesystem

    """

    # Create a dictionary from the input lists in order to generate the graph
    dict = data_structure_utils.create_dictionary(date_list, figures_list)

    fig, ax = plt.subplots()

    ax.set_title(name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    # Format the date to prevent overlapping and make easier to read
    fig.autofmt_xdate()

    # Only output 17 x-axis ticks (representing each quarter over a 4 year period)
    ax.xaxis.set_major_locator(plt.MaxNLocator(17))

    # Format the y-axis ticks to prevent exponential notation
    ax.ticklabel_format(axis='y', style='sci', scilimits=(5, 15))

    ax.plot(sorted(dict.keys()), dict.values())
    plt.tight_layout()
    plt.savefig(f'./graph_outputs/{name}.png')
    print(f"\'{name}.png\' has been saved in the folder : graph_outputs")

def generate_category_figure_pie_chart(categories_list: list, figures_list: list, name, x_label="", y_label=""):
    """
        This function is designed to take in two lists and generate a Pie Chart

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - A graph is saved to the filesystem

    """

    # Create a dictionary from the input lists in order to generate the graph
    dict = data_structure_utils.create_dictionary(categories_list, figures_list)

    fig, ax = plt.subplots()

    ax.set_title(name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    ax.pie(dict.values(), labels=dict.keys(), autopct='%1.1f%%')
    plt.tight_layout()
    plt.savefig(f'./graph_outputs/{name}.png')
    print(f"\'{name}.png\' has been saved in the folder : graph_outputs")

def generate_category_figure_barchart(categories_list: list, figures_list: list, name, x_label="", y_label=""):
    """
        This function is designed to take in two lists and generate a Bar Chart

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - A graph is saved to the filesystem

    """

    # Create a dictionary from the input lists in order to generate the graph
    dict = data_structure_utils.create_dictionary(categories_list, figures_list)

     # If the categories list is the list of regions, remove negligible states as it skews the graph
    if "TotalUS" in dict:
       dict = {k: v for k, v in dict.items() if v >= 150000000}

    fig, ax = plt.subplots()

    y_pos = [i for i in range(len(dict))]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dict.keys())

    ax.set_title(name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    # Format the x-axis ticks to prevent exponential notation
    ax.ticklabel_format(axis='x', style='sci', scilimits=(5, 15))

    ax.barh(y_pos, dict.values(), align="center")
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.savefig(f'./graph_outputs/{name}.png')
    print(f"\'{name}.png\' has been saved in the folder : graph_outputs")

def generate_basic_boxplot(list_of_figures, name="", x_label="", y_label=""):
    """
        This function is designed to take in a list and generate a Box Plot

        Parameters
        ----------
        figures_list - The values that will be represented on the box plot
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - A graph is saved to the file system

    """
    fig, ax = plt.subplots()

    ax.set_title(name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    ax.boxplot(list_of_figures, showfliers=False)

    # Format the y-axis ticks to prevent exponential notation
    ax.ticklabel_format(axis='y', style='sci', scilimits=(2, 15))

    plt.tight_layout()
    plt.savefig(f'./graph_outputs/{name}.png')
    print(f"\'{name}.png\' has been saved in the folder : graph_outputs")

def generate_category_figure_boxplot(categories_list, figures_list, category_identifier, name="", x_label="", y_label=""):
    """
        This function is designed to take in two lists and an identifier in order to output a unique Boxplot

        Parameters
        ----------
        categories_list - A categorical set of values
        figures_list - A set of figures where each figure corresponds to a category
        category_identifier - a parameter present in the categories_list to narrow down the figures_list
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - Function calls generate_basic_boxplot to generate a boxplot

    """

    # Uee category_identifier to only get data for that category before creating an individual box plot
    list_of_figures = [value for key, value in zip(categories_list, figures_list) if key == category_identifier]

    generate_basic_boxplot(list_of_figures, name, x_label, y_label)


def generate_barchart_boxplot(categories_list, figures_list, name, x_label="", y_label=""):

    """
        This function takes in a list of values, a list of figures and a parameter

        Parameters
        ----------
        list of figures - The values that will be repersented on the box plot
        list of categories - a list of categories, once category will be chosen to narrow down the list of values
        name - The Title of the graph
        x_label - The label for the x-axis
        y_label - The label for the y-axis

        Returns
        -------
        No Return Type - A graph is saved to the file system

    """

    dict = {dict_key : [ list_value for list_key, list_value in zip(categories_list, figures_list) if list_key == dict_key ] for dict_key in categories_list}

    fig, ax = plt.subplots()

    ax.set_title(name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    # Format the y-axis ticks to prevent exponential notation
    ax.ticklabel_format(axis='x', style='sci', scilimits=(5, 15))

    # Format the y-axis ticks to create a bit more room
    plt.setp(ax.get_yticklabels(), fontsize=10)

    ax.boxplot(dict.values(), vert=False, labels=dict.keys(), showfliers=False)

    plt.tight_layout()
    plt.savefig(f'./graph_outputs/{name}.png')
    print(f"\'{name}.png\' has been saved in the folder : graph_outputs")