# verbs_usage

**usage_verbs.py** check folder with .py files to list most common verbs used in functions names
and print to standard output short statistics. It can be used as standalone program, or to be imported

## Sample output when run as standalone program
```
python usage_verbs.py test_folder

11 .py files, used 33 verbs in function names(6 unique), 5 most common verbs are: [('get', 21), ('take', 4), ('make', 3), ('save', 3), ('remove', 1)]

Process finished with exit code 0
```

## Using as external module

function find_verbs_in_python_code has 2 kew word arguments:
- path_name - path to directory to be checked
- max_common - number of most common verbs to be found, default value is 5
```
import sys
from verbs_usage import find_verbs_in_python_code


if __name__ == '__main__':
    python_project_directory = sys.argv[1]
    find_verbs_in_python_code(path_name=python_project_directory, max_common=6)
```

## Requirements
**usage_verbs.py** is written in Python 3.6.1, and requires module ***pos_tag** from package **nltk** ver 3.2.4


