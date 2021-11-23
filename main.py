from study_data import get_all_programs_list
from pprint import pprint


if __name__ == '__main__':
    all_programs = get_all_programs_list()
    for program1 in all_programs:
        print(program1['name'])