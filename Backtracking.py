import init as it
import numpy as np
import time as t


crossword = it.modify_crossword_edges("crossword_CB.txt")
u_variables = it.extract_variables(crossword)
words = it.extract_domain("diccionari_A.txt",u_variables)

a_variables = np.zeros(len(u_variables),dtype=bool)
length  = crossword.shape[0]
width = crossword.shape[1]
done = False

crossword = np.zeros((crossword.shape[0],crossword.shape[1]),dtype='S1').flatten()
iter = 0


def modify_domain(var):


    d = words[u_variables[var].size]

    for i in range(crossword[u_variables[var]].shape[0]):
        if crossword[u_variables[var]][i]:
            d = d[d[:,i] == crossword[u_variables[var][i]],:]


    return d,crossword[u_variables[var]]


def assign_next_var(var):

    """
    :return: 
    """

    for i in range(len(u_variables)):

        if np.any(np.in1d(u_variables[var],u_variables[i])) and not a_variables[i]:
            next_var = i
            return next_var

    for i in range(len(a_variables)):
        if not a_variables[i]:
            next_var = i
            return next_var


def Backtracking(var):

    #hello.append("hello")
    global iter
    global done

    iter += 1

    if False not in a_variables:
        done = True
        return np.reshape(crossword,(length,width))



    a_variables[var] = True
    domain,pos = modify_domain(var)
    next_var = assign_next_var(var)

    for word in domain:
        crossword[u_variables[var]] = word
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
