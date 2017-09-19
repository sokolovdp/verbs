import sys
from verbs_usage import find_verbs_in_python_code


python_project_directory = sys.argv[1]
find_verbs_in_python_code(path_name=python_project_directory, max_common=5)
