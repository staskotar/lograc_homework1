import random
import sys

def generate_random_CNF(address, nbvar, nbclauses):
    fo = open(address, "w")
    fo.write("c random cnf file\n")
    fo.write("p cnf " + str(nbvar) + " " + str(nbclauses) + "\n")
    for i in range(nbclauses):
        clause = ""
        for j in range(1, nbvar):
            sign = random.randint(-1, 1)
            if sign != 0:
                clause = clause + str(sign*j) + " "
        fo.write(clause + "0 \n")
    fo.close()


def main(args):
    if len(args) != 5:
        raise ValueError("Please provide an output file name, nbvar, nbclauses and seed")
    if args[1][0] != "'" or args[1][-5:] != ".txt'":
        raise ValueError("File name has to be in the format 'filename.txt'")
    if args[2][0] != "'" or args[2][-1] != "'" or args[3][0] != "'" or args[3][-1] != "'" or args[4][0] != "'" or args[4][-1] != "'":
        raise ValueError("nbvar, nbclauses and seed have to be in the format 'x'")
    random.seed(int(args[4][1:-1]))
    generate_random_CNF(args[1][1:-1], int(args[2][1:-1]), int(args[3][1:-1]))


if __name__ == '__main__':
    main(sys.argv)
