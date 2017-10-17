import init as it
import numpy as np
import time as t
from collections import OrderedDict

crossword = it.modify_crossword_edges("crossword_A.txt")
u_variables = it.extract_variables(crossword)
words = it.extract_domain("diccionari_A.txt",u_variables)

a_variables = np.zeros(len(u_variables),dtype=bool)
length  = crossword.shape[0]
width = crossword.shape[1]
done = False
m_domain = OrderedDict()
count = 0


crossword = np.array([' '] * length * width,dtype='S1').reshape((crossword.shape[0],crossword.shape[1])).flatten()
iter = 0


def modify_domain(var):



    d = words[u_variables[var].size]

    for i in range(crossword[u_variables[var]].shape[0]):
        if crossword[u_variables[var]][i] != ' ':
            d = d[d[:,i] == crossword[u_variables[var][i]],:]


    return d, crossword[u_variables[var]]

def forward_checking(var):

    """
    :return: 
    """

    for i in range(len(u_variables)):

        intersect = np.in1d(u_variables[var], u_variables[i])

        if np.any(intersect) and not a_variables[i] and var != i:

            d = words[u_variables[i].size]
            c = crossword[u_variables[i]]

            for i in range(c.size):
                if c[i] != ' ':
                    d = d[d[:,i] == c[i], :]

            m_domain[i] = d


            if m_domain[i].size == 0:
                    return False



    return True



def assign_next_var(var):

    for i in range(a_variables.size):
        if np.any(np.in1d(u_variables[var],u_variables[i])) and not a_variables[i]:
            next_var = i
            return next_var

    for i in range(a_variables.size):
        if not a_variables[i]:
            next_var = i
            return next_var


def Backtracking(var):

    global iter
    global done
    global count

    iter += 1
    if False not in a_variables:
        done = True
        return np.reshape(crossword,(length,width))



    domain,pos = modify_domain(var)

    for word in domain:

        crossword[u_variables[var]] = word

        if forward_checking(var):
            a_variables[var] = True
            next_var = assign_next_var(var)
            res = Backtracking(next_var)

        if done:
            return res


        crossword[u_variables[var]] = pos

    a_variables[var] = False
    return None

time = t.time()
print Backtracking(assign_next_var(0))
print iter
print "Total Time: %f" % (t.time() - time)

