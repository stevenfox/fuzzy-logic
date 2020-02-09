import sys
import os


file_rules = 'files/rules.txt'
file_fuzzy_set = 'files/fuzzy_set.txt'
file_membership = 'files/membership_var.txt'


def search(values, searchFor, list_index):
    list_values = values.split()
    for i in list_values:
        if searchFor in i:
            return list_values[list_index]
    return None


def rule_set_parser():
    _filepath = file_rules
    rule_dict = {}
    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()

    lines = open(file_rules).readlines()

    for l in lines:
        (key, val) = l.strip().split(':')
        rule_dict[key] = val

    _dic_indx = 1
    if_word = 'If'

    rule_set_dict = {}

    for i in rule_dict:
        if "Rule " + str(_dic_indx) in i:
            if if_word in rule_dict[i]:
                rule_set_dict.update({'first_var_'+str(_dic_indx): search(
                    rule_dict[i], if_word, 1)})

            rule_set_dict.update(
                {'first_val_'+str(_dic_indx): search(rule_dict[i], if_word, 3)})
            rule_set_dict.update(
                {'operator_'+str(_dic_indx): search(rule_dict[i], if_word, 4)})
            rule_set_dict.update(
                {'second_var_'+str(_dic_indx): search(rule_dict[i], if_word, 5)})
            rule_set_dict.update(
                {'second_val_'+str(_dic_indx): search(rule_dict[i], if_word, 7)})
            rule_set_dict.update(
                {'result_var_'+str(_dic_indx): search(rule_dict[i], if_word, 9)})
            rule_set_dict.update(
                {'result_val_'+str(_dic_indx): search(rule_dict[i], if_word, 11)})

        else:
            print("No Rules found")
        _dic_indx += 1

    # print("set\n", rule_set_dict)

    return rule_set_dict


def fuzzy_set_parser():

    _filepath = file_fuzzy_set
    fuzzy_dict = {}
    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()

    lines = open(file_fuzzy_set).readlines()

    counter = 0
    for l in lines:
        val = l.split()
        fuzzy_dict[counter] = val
        counter += 1

    # print(fuzzy_dict)

    _dic_indx = 1
    _tupple_indx = 1

    fuzzy_set_dict = {}

    for i in fuzzy_dict:
        # print('fuzzy? :) ', _dic_indx, ' ', fuzzy_dict[i])
        if(len(fuzzy_dict[i]) > 1):
            fuzzy_set_dict.update(
                {'Tuple_'+str(_tupple_indx): fuzzy_dict[i]})
            fuzzy_4_tuple = fuzzy_dict[i][1]+fuzzy_dict[i][2] + \
                fuzzy_dict[i][3]+fuzzy_dict[i][4]
            # print('fuzzyy Class : ', Tupple.low)
            _tupple_indx += 1
        elif (len(fuzzy_dict[i]) == 1):
            fuzzy_set_dict.update(
                {'Title_'+str(_tupple_indx): fuzzy_dict[i]})
            _tupple_indx += 1
            # print('\nTitles: ', fuzzy_dict[i])

        _dic_indx += 1

    print(fuzzy_set_dict['Tuple_6'][0], fuzzy_set_dict['Tuple_6'][1], fuzzy_set_dict['Tuple_6'][2], fuzzy_set_dict['Tuple_6']
          [3], fuzzy_set_dict['Tuple_6'][4])

    return fuzzy_set_dict


def main():
    rule_set_parser()
    # print('fuzzy      ', fuzzy_set_parser())
    fuzzy_set_parser()


if __name__ == '__main__':
    main()
