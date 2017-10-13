import numpy as np

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

    crossword_flattened = list(crossword_map.flatten())


    # Extract variables from crossword and the squares they occupy variables
    for i in range(1,len(crossword_flattened)):
        # Horizontal variables
        if crossword_flattened[i - 1] == "#" and "0" != crossword_flattened[i] and "#" != crossword_flattened[i]:
            variables.append([i])

            for j in range(1,crossword_flattened[i:].index("#")):
                variables[-1].append(i + j)

        #Vertical variables
        if crossword_flattened[i - crossword_map.shape[1]] == "#" and "0" != crossword_flattened[i] and "#" != crossword_flattened[i]:
            variables.append([i])

            for j in range(crossword_map.shape[1],len(crossword_flattened),crossword_map.shape[1]):
                if crossword_flattened[i + j] == "#":
                    break
                variables[-1].append(i + j)

    final_variables = []
    for j in range(len(variables)):
        #Builds list of of tuples e.g( [(word,collision, collision), ... ])
        final_variables.append([(i,variables[i].index(list(set(variables[j]) & set(variables[i]))[0]),
                                 variables[j].index(list(set(variables[i]) & set(variables[j]))[0]))
                                 for i in range(len(variables)) if set(variables[i]) & set(variables[j]) and i != j])


    return final_variables,[len(var) for var in variables]


def extract_domain(filename,variables):
    """
    :param filename: path to file with the dictionary to load
    :return: numpy array where each position represents a word in the dictionary
    
    """
    words = np.loadtxt(filename,delimiter="\n",dtype="S")
    domain = {}

    for i in set(variables):
        char_array = np.array([list(word) for word in words if len(word) == i])
        keys = [v for v in variables if v == i]
        domain.update({key:char_array for key in keys})


    return domain
