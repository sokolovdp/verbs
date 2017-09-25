from nltk import pos_tag
from collections import Counter


def count_proper_words(names: "list", word_type: "str") -> 'dict':
    def is_proper_type(word: "str") -> "bool":
        return pos_tag([word])[0][1] == word_type

    all_proper_words = []
    for name in names:
        verbs = [word for word in name.split('_') if word and is_proper_type(word)]
        if verbs:
            all_proper_words.extend(verbs)
    return dict(Counter(all_proper_words))


def sum_two_dicts(dict_one: "dict", dict_two: "dict") -> "dict":
    return {key: dict_one.get(key, 0) + dict_two.get(key, 0) for key in set(dict_one.keys()) | set(dict_two.keys())}


def analyse_parsed_data(parsed_data: "list") -> "tuple":
    all_result_data = []
    sum_func_vbs = {}
    sum_func_nns = {}
    sum_vars_vbs = {}
    sum_vars_nns = {}
    for file_data in parsed_data:
        verbs_in_functions = count_proper_words(file_data['result']['functions'], 'VB')
        nouns_in_functions = count_proper_words(file_data['result']['functions'], 'NN')
        verbs_in_variables = count_proper_words(file_data['result']['variables'], 'VB')
        nouns_in_variables = count_proper_words(file_data['result']['variables'], 'NN')
        file_analysis_result = {'file': file_data['file'],
                                'func_VBs': verbs_in_functions,
                                'func_NNs': nouns_in_functions,
                                'vars_VBs': verbs_in_variables,
                                'vars_NNs': nouns_in_variables,
                                }
        all_result_data.append(file_analysis_result)
        sum_func_vbs = sum_two_dicts(sum_func_vbs, verbs_in_functions)
        sum_func_nns = sum_two_dicts(sum_func_nns, nouns_in_functions)
        sum_vars_vbs = sum_two_dicts(sum_vars_vbs, verbs_in_variables)
        sum_vars_nns = sum_two_dicts(sum_vars_nns, nouns_in_variables)

    return all_result_data, {'sum_func_vbs': sum_func_vbs, 'sum_func_nns': sum_func_nns,
                             'sum_vars_vbs': sum_vars_vbs, 'sum_vars_nns': sum_vars_nns, }
