import sys
from verbs_usage import find_verbs_in_python_code


if __name__ == '__main__':
    python_project_directory = sys.argv[1]
    find_verbs_in_python_code(path_name=python_project_directory, max_common=5)
