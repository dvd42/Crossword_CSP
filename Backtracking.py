def modify_domain(domain,var,word,u_variables):

    copy_domain = domain.copy()

    for v in u_variables:
        if v[0][0] != var[0][0]:
            matches = set(var[1]) & set(v[1])

            for match in matches:
                new_domain = []
                if v[0] + "m" in copy_domain and copy_domain[v[0] + "m"]:
                    [new_domain.append(w) for w in copy_domain[v[0] + "m"] if
                     w[v[1].index(match)] == word[var[1].index(match)]]

                else:
                    [new_domain.append(w) for w in copy_domain[str(len(v[1]))] if
                     w[v[1].index(match)] == word[var[1].index(match)]]

                copy_domain[v[0] + "m"] = new_domain

    return copy_domain

def check_restrictions(words,u_variables,a_variables,var_value,var):
    """
    :param var: variable being analyzed
    :param a_variables: list of assigned variables
    :return: True if all restrictions are satisfied, False otherwise
    
    """


    for v in u_variables:
        if v[0] + "m" in words:
            if not words[v[0] + "m"]:
                return False


    # Find words that intersect with the variable that is being analyzed
    """
    for v in a_variables:
        if v[0][0][0] != var[0][0]:
            matches = list(set(var[1]) & set(v[0][1]))
            if matches:
                # Check that the current variable satisfies the restrictions
                for match in matches:
                    if v[1][v[0][1].index(match)] != var_value[var[1].index(match)]:
                        return False

    """
    return True


def Backtracking(a_variables,u_variables,words):
    """
    :param a_variables: list of tuples holding the name and absolute position of assigned variables
    :param u_variables: list of tuples holding the name and absolute position of unassigned variables
    :param words: dictionary with all the words to fill the crossword
    :param size: number of variables
    :return: 
    
    """
    if not u_variables:
        return a_variables

    #domain_size = len(words)
    var = u_variables[-1]


    if var[0] + "m" in words:
        x = var[0] + "m"
    else:
        x = str(len(var[1]))

    for word in words[x]:
        copy_words = modify_domain(words, var, word, u_variables)
        if check_restrictions(copy_words,u_variables,a_variables,var,word):
            res = Backtracking(a_variables + [(var,word)],u_variables[:-1],copy_words)
            if res != None:
                return res


    return None