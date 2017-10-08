import init as it
import Backtracking as bck


def main():

    crossword = it.modify_crossword_edges("crossword_CB.txt")
    u_variables = it.extract_variables(crossword)
    words = it.extract_domain("diccionari_CB.txt",u_variables)
    a_variables = []

    print bck.Backtracking(a_variables, u_variables, words)


if __name__ == "__main__":
    main()
