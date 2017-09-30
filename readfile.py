import numpy as np

crossword_map = np.loadtxt("crossword_CB.txt",delimiter="\t", comments="!",dtype="S2")


def extract_variables(crossword_map):

    """
    :param crossword_map: 2D-numpy array with the crossword map 
    :return: a dictionary of tuples holding the position and length of each word in the crossword 
    """

    #Surround the matrix with #
    crossword_map = np.insert(crossword_map,0,"#",axis=1)
    crossword_map = np.insert(crossword_map,crossword_map.shape[0],"#",axis=1)
    crossword_map = np.insert(crossword_map,0,"#",axis=0)
    crossword_map = np.insert(crossword_map,crossword_map.shape[0],"#",axis=0)

    variables = {}

    a = list(crossword_map.flatten())

    #Extract variables from crossword
    for i in range(1,len(a)):
        if a[i - 1] == "#" and "0" != a[i] and "#" != a[i]:
            variables["v" + str(a[i])] = (np.argwhere(crossword_map == a[i]),0)
        if a[i - crossword_map.shape[1]] == "#" and "0" != a[i] and "#" != a[i]:
            variables["h" + str(a[i])] = (np.argwhere(crossword_map == a[i]),0)

    return variables


print extract_variables(crossword_map)