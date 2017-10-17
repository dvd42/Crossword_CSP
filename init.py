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
    :param crossword_map holds the crossword 
    :type crossword_map 2D-numpy array
    :return list holding all the variables and their absolute position on the board
    :rtype list holding 1D-numpy arrays
    """
    variables = []

    crossword_flattened = list(crossword_map.flatten())


    # Extract variables from crossword and the squares they occupy variables
    for i in range(crossword_map.shape[0],len(crossword_flattened)):
        # Horizontal variables
        if crossword_flattened[i - 1] == "#" and "0" != crossword_flattened[i] and "#" != crossword_flattened[i]:
            variables.append(np.array([],dtype='uint8'))
            variables[-1] = np.append(variables[-1],[i])

            for j in range(1,crossword_flattened[i:].index("#")):
                variables[-1] = np.append(variables[-1], [i+j])


        #Vertical variables
        if crossword_flattened[i - crossword_map.shape[1]] == "#" and "0" != crossword_flattened[i] and "#" != crossword_flattened[i]:
            variables.append(np.array([],dtype='uint8'))
            variables[-1] = np.append(variables[-1], [i])
            for j in range(crossword_map.shape[1],len(crossword_flattened),crossword_map.shape[1]):
                if crossword_flattened[i + j] == "#":
                    break
                variables[-1] = np.append(variables[-1], [i + j])


    return variables


def extract_domain(filename,variables):
    """
    :param filename: path to file with the dictionary to load
    :type filename: string
    :param variables: holds all the variables and their absolute position on the board
    :type variables: list holding 1D-numpy arrays
    :return dictionary holding the length of the variable and all the words with that length read from 'filename'
    :rtype dictionary {key = int, value=numpy array}
    """
    words = np.loadtxt(filename,delimiter="\n",dtype="S")
    domain = {}

    #Build the dictionary
    for v in variables:
        domain.update({v.size: np.array([list(word) for word in words if len(word) == v.size])})
    return domain
