
import sys

from src.parser import parse
from src.Environment import create_table_of_truth, Environment

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    axioms, queries, list_rules = parse(sys.argv[1])
    # print("axioms:", axioms)
    # print("queries:", queries)
    # print("list_rules")
    # for i in list_rules:
    #     print(str(i))
    table = create_table_of_truth(list_rules, axioms)
    env = Environment(list_rules, table)
    print(str(env))

if __name__ == "__main__":
    main()