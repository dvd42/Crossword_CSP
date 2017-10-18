import init as it
import numpy as np
import time as t
import sys
if len(sys.argv) != 3:
	print "Usage: Backtracking.py crosswordfile diccionarifile"
	sys.exit()

crossword = it.modify_crossword_edges(sys.argv[1])
u_variables = it.extract_variables(crossword)
words = it.extract_domain(sys.argv[2],u_variables)

# Boolean numpy array where (array[x] = True if the variable x has been assigned)
a_variables = np.zeros(len(u_variables),dtype=bool)
length  = crossword.shape[0]
width = crossword.shape[1]

# True if a solution has been found
done = False

# Dictionary holding the modified domains for each unassigned variable (key: int, val: (2D numpy array)
m_domain = {}

#Build the crossword to fill it with the words
crossword = np.array(['#'] * length * width,dtype='S1').reshape((crossword.shape[0],crossword.shape[1])).flatten()



def modify_domain(var):
    """
    :param var: variable analyzed in this recursive call
    :type var int
    :return var's new domain, the state of the positions occupied by var in the crossword
    :rtype int,1D-numpy array
    """

    d = words[u_variables[var].size]

    #Reduces var's domain only to the words that satisfy the restrictions (letters in all the right places)
    for i in range(crossword[u_variables[var]].shape[0]):
        if crossword[u_variables[var]][i] != '#':
            d = d[d[:,i] == crossword[u_variables[var][i]],:]


    return d, crossword[u_variables[var]]

def forward_checking(var):

    """
    :param var: variable analyzed in this recursive call
    :type var int
    :return: False if any domain is left empty by var's assignation. True otherwise
    """

    for i in range(len(u_variables)):
        intersect = np.in1d(u_variables[var], u_variables[i])

        # If an assigned and unassigned variable meet in the crossword the domain of the unassigned variable will be updated
        if np.any(intersect) and not a_variables[i] and var != i:
            d = words[u_variables[i].size]
            c = crossword[u_variables[i]]

            for i in range(c.size):
                if c[i] != '#':
                    d = d[d[:,i] == c[i], :]
            m_domain[i] = d
            if m_domain[i].size == 0:
                    return False
    return True



def assign_next_var(var):

    """
    
    :param var: variable analyzed in this recursive call
    :return: the variable to be analyzed in the next recursive call
    :rtype int
    """

    # If var meets with another variable the latter will be chosen to be analyzed in the next recursive call
    for i in range(a_variables.size):
        if np.any(np.in1d(u_variables[var],u_variables[i])) and not a_variables[i]:
            next_var = i
            return next_var

    # If var does not meet with any other variable in the crossword the first unassigned variable will be chosen
    for i in range(a_variables.size):
        if not a_variables[i]:
            next_var = i
            return next_var


def Backtracking(var):

    """
    
    :param var: variable analyzed in this recursive call
    :rtype int 
    :return: Full completed crossword if a solution exists. None otherwise
    :rtype 2D-numpy array
    """

    global done

    # If all variables have been assigned a solution has been found
    if False not in a_variables:
        done = True
        return np.reshape(crossword,(length,width))[1:-1,1:-1]

    domain,pos = modify_domain(var)

    for word in domain:
        crossword[u_variables[var]] = word

        if forward_checking(var):
            a_variables[var] = True
            next_var = assign_next_var(var)
            res = Backtracking(next_var)

        if done:
            return res

    # Undo changes in global variables
        crossword[u_variables[var]] = pos

    a_variables[var] = False
    return None


time = t.time()
print Backtracking(assign_next_var(0))
print "Backtracking Time: %f" % (t.time() - time)

