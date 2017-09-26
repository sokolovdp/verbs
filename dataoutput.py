import sys
import json

VALID_OUTPUT_TYPES = ['json', 'csv', 'con']
output_json_file = "code_analyse_result.json"
output_csv_file = "code_analyse_result.csv"


def write_json_file(result_data: "dict"):
    with open(output_json_file, 'w', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(result_data, sort_keys=True, indent=4, ensure_ascii=False))
    print('created json file {} with analysis data'.format(output_json_file))


def printable_str(list_of_tuples: "list") -> "str":
    return str(list_of_tuples).replace(',', '').strip('[]')


def top_n_elements(n: 'int', dictionary: "dict") -> "list":
    return list(dictionary.items())[:n]


def print_to_stdout_or_csv_file(result_data: "dict", max_top: "int", output_type: "str"):
    if output_type == 'con':
        out_channel = sys.stdout
        sep = ' -> '
    else:
        out_channel = open(output_csv_file, 'w', encoding='UTF-8')
        sep = ','

    print("Totals", file=out_channel)
    print("top verbs in func",
          printable_str(top_n_elements(max_top, result_data['totals']['sum_func_vbs'])),
          sep=sep, file=out_channel)
    print("top nouns in func",
          printable_str(top_n_elements(max_top, result_data['totals']['sum_func_nns'])),
          sep=sep, file=out_channel)
    print("top verbs in vars",
          printable_str(top_n_elements(max_top, result_data['totals']['sum_vars_vbs'])),
          sep=sep, file=out_channel)
    print("top nouns in vars",
          printable_str(top_n_elements(max_top, result_data['totals']['sum_vars_nns'])),
          sep=sep, file=out_channel)

    print('Details', file=out_channel)
    for data in result_data['details']:
        print(data['file'], file=out_channel)
        print("top verbs in func",
              printable_str(top_n_elements(max_top, data['func_vbs'])),
              sep=sep, file=out_channel)
        print("top nouns in func",
              printable_str(top_n_elements(max_top, data['func_nns'])),
              sep=sep, file=out_channel)
        print("top verbs in vars",
              printable_str(top_n_elements(max_top, data['vars_vbs'])),
              sep=sep, file=out_channel)
        print("top nouns in vars",
              printable_str(top_n_elements(max_top, data['vars_nns'])),
              sep=sep, file=out_channel)

    if output_type == 'csv':
        out_channel.close()
        print('created csv file {} with analysis data'.format(output_csv_file))


def output_results(result_data: "dict", max_top: "int", out_channel):
    if out_channel in ['con', 'csv']:
        print_to_stdout_or_csv_file(result_data, max_top, "con")
    else:
        write_json_file(result_data)
