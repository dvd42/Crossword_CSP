import init as it

crossword = it.modify_crossword_edges("crossword_A.txt")
u_variables,length = it.extract_variables(crossword)
words = it.extract_domain("diccionari_A.txt", length)
a_variables = [0] * len(u_variables)
a_words = [""] * len(a_variables)
priorities = [0] * len(a_variables)



def modify_domain(var):


    d = words[length[var]]

    for match in u_variables[var]:
        if a_variables[match[0]] != 0:
            d = d[d[:, match[2]] == a_words[match[0]][match[1]], :]

    return d



def assign_next_var():
    """
    
    :return: 
    """
    """
    next_var = 0
    for i in range(len(a_variables)):
        if a_variables[i] != 1:
            next_var = i
            break
    """

    if all(p == 0 for p in priorities):
        list = [len(u_variables[i]) if a_variables[i] != 1 else 0 for i in range(len(a_variables))]
        next_var = list.index(max(list))
    else:
        next_var = priorities.index(max(priorities))

    priorities[next_var] = 0

    for v in u_variables[next_var]:
        if a_variables[v[0]] != 1:
            priorities[v[0]] += 1


    return next_var

def Backtracking(var):


    if 0 not in a_variables:
        return a_words

    a_variables[var] = 1
    domain = modify_domain(var)
    next_var = assign_next_var()

    for word in domain:
        a_words[var] = word
        res = Backtracking(next_var)
        if res != None:
            return res

    a_variables[var] = 0

    for v in u_variables[var]:
        if priorities[v[0]] > 0:
            priorities[v[0]] -= 1

    return None


print Backtracking(assign_next_var())
