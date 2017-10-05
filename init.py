import numpy as np
from collections import defaultdict


class variable:
    def __init__(self, location, orientation, length, tag,value,squares):
        """
        :param location: where the word starts in the matrix
        :param orientation: whether the word is vertical or horizontal
        :param length: how long the word is 
        :param tag:number assigned to the word in crossword (e.g: 1,2,3..n)
        :param value: the word
        :param squares: every square occupied by the word
        """
        self.length = length
        self.location = location
        self.orientation = orientation
        self.tag = tag
        self.value = value
        self.squares = squares


def modify_crossword_edges(filename):

    """
    :param filename: path to the file containing the crossword
    :return: crossword structure stored in a 2D numpy array 
    """
    crossword_map = np.loadtxt(filename, delimiter="\t", comments="!", dtype="S2")

    # Surround the matrix with #
    crossword_map = np.insert(crossword_map, 0, "#", axis=1)
    crossword_map = np.insert(crossword_map, crossword_map.shape[0], "#", axis=1)
    crossword_map = np.insert(crossword_map, 0, "#", axis=0)
    crossword_map = np.insert(crossword_map, crossword_map.shape[0], "#", axis=0)

    return crossword_map


def extract_variables(crossword_map):

    """
    :param crossword_map: 2D-numpy array with the crossword map 
    :return: a list of variable objects 
    """
    variables = []

    a = list(crossword_map.flatten())

    # Extract variables from crossword and assign distance to 'h' variables
    for i in range(1,len(a)):
        if a[i - 1] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            variables.append(variable(np.argwhere(crossword_map == a[i]),'h',a[a.index(a[i]):].index("#"),a[i],"",[]))

        if a[i - crossword_map.shape[1]] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            #TODO use lambda function to calculate 'v' variables lengths
            variables.append(variable(np.argwhere(crossword_map == a[i]), 'v', 0, a[i],"",[]))

    # Assign distance to 'v' variables
    for var in variables:
        if 'v' in var.orientation:
            for i in range(var.location[0][0],crossword_map.shape[0]):
                if crossword_map[i,var.location[0][1]] == "#":
                    var.length = i - var.location[0][0]
                    break

    #Calculate the absolute squares occupied by each variable
    for var in variables:
        var.squares = [var.location[0][0]*crossword_map.shape[1] + var.location[0][1]]

        for i in range(1, var.length):
            if var.orientation == 'v':
                var.squares.append(var.squares[0] + i * crossword_map.shape[1])
            else:
                var.squares.append(var.squares[0] + i)

    return variables


def extract_domain(variables, filename):
    """
    :param variables: list of "variable" objects
    :param filename: path to file with the dictionary to load
    :return: A dictionary where keys are the size of the words to insert in the crossword 
             and the value is every word of that size found in the file
    """

    words = np.loadtxt(filename,delimiter="\n",dtype="S")
    lengths = [var.length for var in variables]
    Domain = defaultdict(list)

    # noinspection PyTypeChecker
    for i in range(min(lengths),max(lengths) + 1):
        for x in words.flatten():
            if len(x) == i:
                Domain[i].append(x)

    return Domain

extract_variables(modify_crossword_edges("crossword_CB.txt"))