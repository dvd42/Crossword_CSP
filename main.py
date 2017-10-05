import init as it
import Backtracking as bck


def main():

    crossword = it.modify_crossword_edges("crossword_A.txt")
    u_variables = it.extract_variables(crossword)
    words = it.extract_domain("diccionari_A.txt")
    a_variables = []

    print bck.Backtracking(a_variables, u_variables, words, len(u_variables))


if __name__ == "__main__":
    main()
