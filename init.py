import numpy as np
from collections import defaultdict,OrderedDict

def modify_crossword_edges(filename):

    """
    :param filename: path to the file containing the crossword
    :return: crossword structure stored in a 2D numpy array 
    
    """
    crossword_map = np.loadtxt(filename, delimiter="\t", comments="!", dtype="S2")
    # Surround the matrix with #
    crossword_map = np.insert(crossword_map, 0, "#", axis=1)
    crossword_map = np.insert(crossword_map, crossword_map.shape[1], "#", axis=1)
    crossword_map = np.insert(crossword_map, 0, "#", axis=0)
    crossword_map = np.insert(crossword_map, crossword_map.shape[0], "#", axis=0)

    return crossword_map


def extract_variables(crossword_map):

    """
    :param crossword_map: 2D-numpy array with the crossword map 
    :return: a dictionary with the variables as keys and the squares they occupy as values (e.g 'h1' = [1,2,3..])
    
    """
    variables = []

    a = list(crossword_map.flatten())


    # Extract variables from crossword and the squares they occupy variables
    for i in range(1,len(a)):
        # Horizontal variables
        if a[i - 1] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            variables.append(("h" + a[i],[i]))

            for j in range(1,a[i:].index("#")):
                variables[-1][1].append(i + j)

        #Vertical variables
        if a[i - crossword_map.shape[1]] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            variables.append(("v" + a[i],[a.index(a[i])]))

            for j in range(crossword_map.shape[1],len(a),crossword_map.shape[1]):
                if a[i + j] == "#":
                    break
                variables[-1][1].append(i + j)

    return variables


def extract_domain(filename,variables):
    """
    :param filename: path to file with the dictionary to load
    :return: numpy array where each position represents a word in the dictionary
    
    """
    words = np.loadtxt(filename,delimiter="\n",dtype="S")
    lengths = [len(var[1]) for var in variables]
    domain =  defaultdict(list)

    for i in words:
        if len(i) in set(lengths):
            domain[str(len(i))].append(i)

    domain = OrderedDict(domain)
    return domain

