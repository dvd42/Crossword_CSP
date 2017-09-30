import numpy as np

class variable:
    def __init__(self,location,orientation,distance,tag):
        """
        :param location: where the word starts in the matrix
        :param orientation: whether the word is vertical or horizontal
        :param distance: how long the word is 
        :param tag:number assigned to the word in crossword (e.g: 1,2,3..n)
        """
        self.distance = distance
        self.location = location
        self.orientation = orientation
        self.tag = tag

def modify_crossword_edges():

    """
    :return: crossword structure stored in a 2D numpy array 
    """
    crossword_map = np.loadtxt("crossword_CB.txt", delimiter="\t", comments="!", dtype="S2")

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

    #Extract variables from crossword and assign distance to 'h' variables
    for i in range(1,len(a)):
        if a[i - 1] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            variables.append(variable(np.argwhere(crossword_map == a[i]),'h',a[a.index(a[i]):].index("#"),a[i]))

        if a[i - crossword_map.shape[1]] == "#" and "0" != a[i] and "#" != a[i]:
            # noinspection PyTypeChecker
            variables.append(variable(np.argwhere(crossword_map == a[i]), 'v', 0, a[i]))

    #Assign distance to 'v' variables
    for var in variables:
        if 'v' in var.orientation:
            for i in range(var.location[0][0],crossword_map.shape[0]):
                if crossword_map[i,var.location[0][1]] == "#":
                    var.distance = i - var.location[0][0]
                    break

    return variables


extract_variables(modify_crossword_edges())