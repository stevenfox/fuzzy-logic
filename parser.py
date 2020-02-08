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
    filepath = file_rules
    rule_dict = {}
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    lines = open(file_rules).readlines()

    for l in lines:
        (key, val) = l.strip().split(':')
        rule_dict[key] = val

    dic_indx = 1
    if_word = 'If'

    rule_set_dict = {}

    for i in rule_dict:
        if "Rule " + str(dic_indx) in i:
            if if_word in rule_dict[i]:
                rule_set_dict.update({'first_var_'+str(dic_indx): search(
                    rule_dict[i], if_word, 1)})

            rule_set_dict.update(
                {'first_val_'+str(dic_indx): search(rule_dict[i], if_word, 3)})
            rule_set_dict.update(
                {'operator_'+str(dic_indx): search(rule_dict[i], if_word, 4)})
            rule_set_dict.update(
                {'second_var_'+str(dic_indx): search(rule_dict[i], if_word, 5)})
            rule_set_dict.update(
                {'second_val_'+str(dic_indx): search(rule_dict[i], if_word, 7)})
            rule_set_dict.update(
                {'result_var_'+str(dic_indx): search(rule_dict[i], if_word, 9)})
            rule_set_dict.update(
                {'result_val_'+str(dic_indx): search(rule_dict[i], if_word, 11)})

        else:
            print("No Rules found")
        dic_indx += 1

    print("set\n", rule_set_dict)


def main():
    rule_set_parser()


if __name__ == '__main__':
    main()
