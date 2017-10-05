import init as it


def check_restrictions(var, var_value, a_variables,max_length):
    """
    :param var: variable being analyzed
    :param a_variables: list of assigned variables
    :param max_length: size of biggest word in the crossword
    :return: True if all restrictions are satisfied, False otherwise
    """

    if not a_variables:
        return True

    # Find words that intersect with the variable that is being analyzed
    for v in a_variables:
        if v.orientation != var.orientation:
            matches = list(set(var.squares) & set(v.squares))
            if matches:
                # Check that the current variable satisfies the restrictions
                for match in matches:
                   if v.value[v.squares.index(match)] != var_value[var.squares.index(match)]:
                       return False

    return True



def Backtracking(a_variables, u_variables, domain,size):
    """
    :param a_variables: list of assigned variables
    :param u_variables: list of unassigned variables
    :param domain: dictionary holding all words 
    :param max_length: size of the longest word in the crossword
    :param size: number of variables
    :return: list with all variables assigned or None if failure
    """

    res = []

    if not u_variables:
        return a_variables

    var = u_variables.pop(-1)
    d = var.length

    for word in domain[d]:
        if check_restrictions(var,word,a_variables,max_length):
            var.value = word
            a_variables.append(var)
            print var.tag,var.orientation,var.value
            res.append(Backtracking(a_variables,u_variables,domain,size))

            res = filter(lambda a: a != None, res)
            if len(res) == size:
                return res


    return None


crossword = it.modify_crossword_edges("crossword_CB.txt")
variables = it.extract_variables(crossword)
domain = it.extract_domain(variables, "diccionari_CB.txt")


size = len(variables)
a_variables = []


res = Backtracking(a_variables,variables,domain,size)



