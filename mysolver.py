import sys


def read_clauses(address):
    fo = open(address, "r")
    all_clauses = fo.read()
    lines = list(all_clauses.split("\n"))
    clauses = []
    for i in lines[3:-1]:
        line = i[:-3]
        clauses.append(list(map(int, list(line.split(" ")))))
    fo.close()
    return clauses


def print_solution_to_file(address, valuation):
    fo = open(address, "w")
    if valuation is None:
        fo.write("0")
    else:
        fo.write(' '.join(map(str, valuation)))
    fo.close()


def check_empty(clauses):
    for i in clauses:
        if i:
            return False
    return True


def check_unit(clauses):
    for i in clauses:
        if len(i) == 1:
            return i[0]
    return 0


def check_pure(clauses):
    index = {}
    for i in clauses:
        for j in i:
            if abs(j) not in index:
                index[abs(j)] = j
            elif index[abs(j)] != j:
                index[abs(j)] = 0
    for k in index:
        if index[k] != 0:
            return index[k]
    return 0


def naive_choice(clauses):
    return clauses[0][0]


def eliminate_variable(clauses, literal):
    clauses = [i for i in clauses if literal not in i]
    clauses = [[k for k in j if k != -literal] for j in clauses]
    return clauses


def sat_solver(clauses):
    if not clauses:
        return []
    elif check_empty(clauses):
        return None
    assignment = check_unit(clauses)
    if assignment:
        reduced_clauses = eliminate_variable(clauses, assignment)
        valuation = sat_solver(reduced_clauses)
        if valuation is None:
            return None
        else:
            valuation.append(assignment)
            return valuation
    assignment = check_pure(clauses)
    if assignment:
        reduced_clauses = eliminate_variable(clauses, assignment)
        valuation = sat_solver(reduced_clauses)
        if valuation is None:
            return None
        else:
            valuation.append(assignment)
            return valuation
    assignment = naive_choice(clauses)
    reduced_clauses = eliminate_variable(clauses, assignment)
    valuation = sat_solver(reduced_clauses)
    if valuation is None:
        reduced_clauses = eliminate_variable(clauses, -assignment)
        valuation = sat_solver(reduced_clauses)
        if valuation is None:
            return None
        else:
            valuation.append(assignment)
            return valuation
    else:
        valuation.append(assignment)
        return valuation


def main(args):
    if len(args) != 3:
        raise ValueError("Please provide both input and output file names")
    if args[1][0] != "'" or args[1][-5:] != ".txt'" or args[2][0] != "'" or args[2][-5:] != ".txt'":
        raise ValueError("File names have to be in the format 'filename.txt'")
    clauses = read_clauses(args[1][1:-1])
    valuation = sat_solver(clauses)
    print_solution_to_file(args[2][1:-1], valuation)


if __name__ == '__main__':
    main(sys.argv)
