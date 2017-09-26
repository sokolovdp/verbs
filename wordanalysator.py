from nltk.corpus import wordnet
from collections import Counter
import operator

from codeparsers import load_words_from_file

EXCEPTIONS = load_words_from_file('verbs_exclusions')  # list of verbs to be treated as nouns
NOUNS = {word.name().split('.', 1)[0] for word in wordnet.all_synsets('n')}
VERBS = {word.name().split('.', 1)[0] for word in wordnet.all_synsets('v')} - EXCEPTIONS


def sort_dictionary_by_value(dictionary: "dict") -> "dict":
    return dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))


def split_word_list_to_verbs_and_nouns(names: "list") -> 'tuple':
    all_verbs = []
    all_nouns = []
    for name in names:
        for word in [part for part in name.split('_')]:
            if word in VERBS:
                all_verbs.append(word)
            elif word in NOUNS:
                all_nouns.append(word)
    return sort_dictionary_by_value(Counter(all_verbs)), sort_dictionary_by_value(Counter(all_nouns))


def sum_two_dicts(dict_one: "dict", dict_two: "dict") -> "dict":
    new_dict = {key: dict_one.get(key, 0) + dict_two.get(key, 0) for key in
                (set(dict_one.keys()) | set(dict_two.keys()))}
    return new_dict


def analyse_parsed_data(parsed_data: "list") -> "dict":
    all_result_data = []
    sum_func_vbs = dict()
    sum_func_nns = dict()
    sum_vars_vbs = dict()
    sum_vars_nns = dict()
    for file_data in parsed_data:
        verbs_in_functions, nouns_in_functions = split_word_list_to_verbs_and_nouns(file_data['result']['functions'])
        verbs_in_variables, nouns_in_variables = split_word_list_to_verbs_and_nouns(file_data['result']['variables'])
        file_analysis_result = {'file': file_data['file'],
                                'func_vbs': verbs_in_functions,
                                'func_nns': nouns_in_functions,
                                'vars_vbs': verbs_in_variables,
                                'vars_nns': nouns_in_variables,
                                }
        all_result_data.append(file_analysis_result)

        sum_func_vbs = sum_two_dicts(sum_func_vbs.copy(), verbs_in_functions)
        sum_func_nns = sum_two_dicts(sum_func_nns.copy(), nouns_in_functions)
        sum_vars_vbs = sum_two_dicts(sum_vars_vbs.copy(), verbs_in_variables)
        sum_vars_nns = sum_two_dicts(sum_vars_nns.copy(), nouns_in_variables)

    return {'details': all_result_data,
            'totals': {'sum_func_vbs': sort_dictionary_by_value(sum_func_vbs),
                       'sum_func_nns': sort_dictionary_by_value(sum_func_nns),
                       'sum_vars_vbs': sort_dictionary_by_value(sum_vars_vbs),
                       'sum_vars_nns': sort_dictionary_by_value(sum_vars_nns)}
            }
