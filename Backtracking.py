
def check_restrictions(var, var_value, a_variables):
    """
    :param var: variable being analyzed
    :param a_variables: list of assigned variables
    :return: True if all restrictions are satisfied, False otherwise
    
    """


    if len(var[1]) != len(var_value):
        return False

    if not a_variables:
        return True

    # Find words that intersect with the variable that is being analyzed
    for v in a_variables:
        if v[0][0][0] != var[0][0]:
            matches = list(set(var[1]) & set(v[0][1]))
            if matches:
                # Check that the current variable satisfies the restrictions
                for match in matches:
                   if v[1][v[0][1].index(match)] != var_value[var[1].index(match)]:
                       return False

    return True



def Backtracking(a_variables,u_variables,words,size):
    """
    :param a_variables: list of tuples holding the name and absolute position of assigned variables
    :param u_variables: list of tuples holding the name and absolute position of unassigned variables
    :param words: dictionary with all the words to fill the crossword
    :param size: number of variables
    :return: 
    
    """

    if not u_variables:
        print a_variables
        return a_variables

    var = u_variables[-1]

    #Iterate the entire dictionary to fill the crossword
    for word in words:
        if check_restrictions(var,word,a_variables):
            res = Backtracking(a_variables + [(var,word)],u_variables[:-1],words,size)
            if len(a_variables) == size:
                return res

    return None