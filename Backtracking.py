import numpy as np
import init as it


def check_restrictions(var, var_value, a_variables,max_length):

    """
    :param var: variable being analyzed
    :param a_variables: list of assigned variables
    :param max_length: size of biggest word in the crossword
    :return: True if all restrictions are satisfied, False otherwise
    """

    #Spaghetti code to check for restrictions

    #TODO implement this

    return True


def Backtracking(a_variables, u_variables, domain,max_length,size):
    """
    
    :param a_variables: list of assigned variables
    :param u_variables: list of unassigned variables
    :param domain: dictionary holding all words 
    :param max_length: size of the longest word in the crossword
    :param size: number of variables
    :return: list with all variables assigned or None if failure
    """

    if not u_variables:
        return a_variables

    var = u_variables.pop(-1)
    d = var.length

    for word in domain[d]:
        if check_restrictions(var,word,a_variables,max_length):
            var.value = word
            a_variables.append(var)
            res.append(Backtracking(a_variables,u_variables,domain,max_length,size))
            if len(res) == size:
                print "hello"
                return res

    return None


crossword = it.modify_crossword_edges("crossword_A.txt")
variables = it.extract_variables(crossword)
domain,min_length,max_length = it.extract_domain(variables, "diccionari_A.txt")

res = []
size = len(variables)
a_variables = []

print Backtracking(a_variables,variables,domain,max_length,size)


