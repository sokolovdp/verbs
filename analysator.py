#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse
import sys
import chardet

import codeparsers
import nameanalysator

VALID_OUTPUT_TYPES = ['json', 'csv', 'con']


#     for python_file in all_python_files:
#
#         all_used_verbs.extend(build_list_of_names_from_source_code(python_file))
#
#     most_common_verbs = Counter(all_used_verbs).most_common(max_common)
#
#     print(
#         "checked {} .py files, found {} functions with verbs in names({} unique verbs),
#           {} most common verbs are: {}".format(
#             len(all_python_files),
#             len(all_used_verbs),
#             len(set(all_used_verbs)),
#             max_common,
#             most_common_verbs)
#     )



def load_source_code_from_file(file_name: "str") -> "str":
    with open(file_name, "rb") as file:
        raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    return raw_data.decode(encoding)


def build_list_of_files_with_source_code(path_name="", extension="") -> "list":
    all_code_files_in_the_path = []
    for path, sub_dirs, files in os.walk(path_name):
        for file_name in files:
            if file_name.endswith(extension):
                full_path = os.path.join(path, file_name)
                all_code_files_in_the_path.append(full_path)
    return all_code_files_in_the_path


def parse_source_code_in_folder(path_name: "str", parser: "codeparsers.SourceCodeParser") -> "list":
    all_code_files = build_list_of_files_with_source_code(path_name=path_name, extension=parser.ext)
    if not all_code_files:
        print("folder {} has no source code files with extension {}".format(path_name, parser.ext))
        return []
    all_parsed_data = []
    for code_file in all_code_files:
        source_code = load_source_code_from_file(code_file)
        all_parsed_data.append({'file': code_file, 'result': parser.analyse_source_code(source_code)})
    return all_parsed_data


def check_folder_is_readable(folder_name: "str") -> "str":
    if not os.path.isdir(folder_name):
        raise argparse.ArgumentTypeError("{0} is not a valid path".format(folder_name))
    if not os.access(folder_name, os.R_OK):
        raise argparse.ArgumentTypeError("{0} is not a readable dir".format(folder_name))
    return folder_name


def check_arg_range(value: "str", valid_range: "list") -> "str":
    if not value.lower() in valid_range:
        raise argparse.ArgumentTypeError("wrong value {}, valid values are: {}".format(value, ', '.join(valid_range)))
    return value


def check_ext_range(ext_value: "str"):
    return check_arg_range(ext_value, codeparsers.VALID_CODES_EXTENSIONS)


def check_out_range(out_type: "str"):
    return check_arg_range(out_type, VALID_OUTPUT_TYPES)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='analyses use of verbs and noon in variables and functions names')
    ap.add_argument("folder", type=check_folder_is_readable, action='store', help="folder with code to analyse")
    ap.add_argument("--top", dest="max_top", type=int, action="store", help="number of top used words")
    ap.add_argument("--vb", dest="check_verbs", action="store_true", help="check usage of verbs")
    ap.add_argument("--nn", dest="check_nouns", action="store_true", help="check usage of nouns")
    ap.add_argument('--vrbl', dest='check_vrbl', action='store_true', help="check variables names")
    ap.add_argument('--func', dest='check_func', action='store_true', help="check functions names")
    ap.add_argument("--ext", dest="code_ext", type=check_ext_range, action='store', default='.py',
                    help="extension of files with code")
    ap.add_argument('--out', dest='out_type', type=check_out_range, action='store', default='con',
                    help="out results to JSON file, CSV file, or CONsole")
    args = ap.parse_args(sys.argv[1:])
    if not (args.check_verbs or args.check_nouns):
        ap.error("at least one of these arguments: --vb or --nn has to be provided")
    if not (args.check_vrbl or args.check_func):
        ap.error("at least one of these arguments: --var or --fun has to be provided")

    code_parser = codeparsers.create_code_parser(ext=args.code_ext)

    parsed_data_from_all_files = parse_source_code_in_folder(args.folder, code_parser)

    analysis_data, summarized_data = nameanalysator.analyse_parsed_data(parsed_data_from_all_files)
