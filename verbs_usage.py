#!/usr/bin/env python3
import os
import ast
from collections import Counter
from nltk import pos_tag

# from memory_profiler import profile


def build_list_of_python_files_in_the_path(path_name: "str") -> "list":
    all_python_files_in_the_path = []
    for path, sub_dirs, files in os.walk(path_name):
        for file_name in files:
            if file_name.endswith('.py'):
                full_path = os.path.join(path, file_name)
                all_python_files_in_the_path.append(full_path)
    return all_python_files_in_the_path


def internal_python_function(function_name: "str") -> "bool":
    return function_name.startswith('__') and function_name.endswith('__')


def get_func_names_from_run_code_tree(python_run_code_tree: "list") -> "list":
    return [node.name.lower() for node in ast.walk(python_run_code_tree)
            if isinstance(node, ast.FunctionDef) and not internal_python_function(node.name)
            ]


def is_verb(word: "str") -> "bool":
    return pos_tag([word])[0][1] == 'VB'


def pull_verbs_from_function_name(function_name: "str") -> "list":
    return [word for word in function_name.split('_') if word and is_verb(word)]


def build_list_of_verbs_in_python_file(python_file_name: "str") -> "list":
    with open(python_file_name, 'r', encoding='utf-8') as python_file:
        python_source_code = python_file.read()
    python_run_code_tree = ast.parse(python_source_code)
    used_func_names = get_func_names_from_run_code_tree(python_run_code_tree)
    all_verbs = []
    for func_name in used_func_names:
        verbs = pull_verbs_from_function_name(func_name)
        if verbs:
            all_verbs.extend(verbs)
    return all_verbs


def find_verbs_in_python_code(path_name="", max_common=5):
    assert os.path.exists(path_name)

    all_python_files = build_list_of_python_files_in_the_path(path_name)
    all_used_verbs = []
    for python_file in all_python_files:
        all_used_verbs.extend(build_list_of_verbs_in_python_file(python_file))

    most_common_verbs = Counter(all_used_verbs).most_common(max_common)

    print(
        "checked {} .py files, found {} functions with verbs in names({} unique verbs), {} most common verbs are: {}".format(
            len(all_python_files),
            len(all_used_verbs),
            len(set(all_used_verbs)),
            max_common,
            most_common_verbs)
    )


if __name__ == '__main__':
    import sys

    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        print("invalid path {}".format(dir_name))
    else:
        find_verbs_in_python_code(dir_name)
