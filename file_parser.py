import sys
import os


file_rules = 'files/RuleSet.txt'
file_fuzzy_set = 'files/RuleSet.txt'
file_membership = 'files/RuleSet.txt'


def search(values, searchFor, list_index):
    # print('search: ', values, searchFor, list_index)
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
        # (key, val) = l.strip().split(':')
        # rule_dict[key] = val
        # (key, val) = l.strip().split(':')
        # rule_dict[key] = val
        rule_dict[l] = l
    _dic_indx = 1
    if_word = 'If'

    rule_set_dict = {}
    for i in rule_dict:
        if "Rule " in i:
            if if_word in rule_dict[i]:
                rule_set_dict.update({'first_var_'+str(_dic_indx): search(
                    rule_dict[i], if_word, 3)})
            rule_set_dict.update(
                {'first_val_'+str(_dic_indx): search(rule_dict[i], if_word, 5)})
            rule_set_dict.update(
                {'operator_'+str(_dic_indx): search(rule_dict[i], if_word, 6)})
            rule_set_dict.update(
                {'second_var_'+str(_dic_indx): search(rule_dict[i], if_word, 7)})
            rule_set_dict.update(
                {'second_val_'+str(_dic_indx): search(rule_dict[i], if_word, 9)})
            rule_set_dict.update(
                {'result_var_'+str(_dic_indx): search(rule_dict[i], if_word, 11)})
            rule_set_dict.update(
                {'result_val_'+str(_dic_indx): search(rule_dict[i], if_word, 13)})

        else:
            print("No Rules found")
        _dic_indx += 1

    # print("set\n", rule_set_dict)

    return rule_set_dict


class Fuzzy_set:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def get(self):
        return self.data

    def get_titles(self, dic, keytitle='Title_'):
        self.title_dict = []
        for key in dic:
            if keytitle in key:
                self.title_dict.append(dic[key])
        return self.title_dict

    def get_tuples(self, dic, title, keytitle='Title_', tuples_range=3):
        self.tuple_dict = []
        count = 0

        for key in dic:
            # print(dic)
            count += 1
            if keytitle in key:
                list_tuple = list(dic.values())
                tuple_title = ' '.join(map(str, dic[key]))

                if(str(tuple_title) in title):
                    for j in range(tuples_range):
                        self.tuple_dict.append(list_tuple[count+j])

        if(not bool(self.tuple_dict)):
            print('No tupple title found')

        return self.tuple_dict

    def get_numbers_tuple(self, dic, _cnt=3):
        # print(max(dic[0][1]))
        self.tuple_int = []
        for k in range(_cnt):
            self.tuple_int.append((dic[k][1:]))
        print(self.tuple_int)
        return self.tuple_int

    def max_tuple(self, dic):
        self.max = max(sorted(dic, key=lambda x: x[1], reverse=True)[0])
        # print(max(sorted(dic, key=lambda x: x[1], reverse=True))[:])
        # print(max(sorted(dic, key=lambda x: x[1], reverse=True)[0]))
        return self.max


def fuzzy_set_parser():

    _filepath = file_fuzzy_set
    fuzzy_dict = {}
    f_set = Fuzzy_set()

    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()

    lines = open(file_fuzzy_set).readlines()
    counter = 0

    for l in lines:
        val = l.split()
        fuzzy_dict[counter] = val
        counter += 1

    _tupple_indx = 1
    fuzzy_set_dict = {}

    for i in fuzzy_dict:
        if(len(fuzzy_dict[i]) > 1):
            fuzzy_set_dict.update(
                {'Tuple_'+str(_tupple_indx): fuzzy_dict[i]})
            _tupple_indx += 1
        elif (len(fuzzy_dict[i]) == 1):
            fuzzy_set_dict.update(
                {'Title_'+str(_tupple_indx): fuzzy_dict[i]})
            _tupple_indx += 1

    return fuzzy_set_dict


def membership_set_parser():

    _filepath = file_membership
    membership_dict = {}
    # f_set = Fuzzy_set()

    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()

    lines = open(file_membership).readlines()
    counter = 0

    membership_set_dict = []
    for l in lines:

        if '=' in l:
            # print('GOTSA ', l)
            # print('>>>?', lines)
            str_l = l.replace('=', '')
            val = str_l.split()
            # membership_set_dict.append(l)
            # print('val ', val)
            # membership_set_dict.remove
            membership_dict[counter] = val
            counter += 1
            # print('mem? ', membership_dict)

    _tupple_indx = 1

    # for i in membership_dict:
    #     if(len(membership_dict[i]) > 1):
    #         membership_set_dict.update(
    #             {'membership_name_'+str(_tupple_indx): membership_dict[i]})
    #         _tupple_indx += 1
    #     elif (len(membership_dict[i]) == 1):
    #         membership_set_dict.update(
    #             {'membership_value_'+str(_tupple_indx): membership_dict[i]})
    #         _tupple_indx += 1

    # print('?? :O', membership_set_dict)
    # print('?? :O', membership_set_dict)

    return membership_dict


def main():
    # rules_set = rule_set_parser()

    # print('rules      ', rules_set)

    x1 = Fuzzy_set()

    # print(x1.add(fuzzy_set_parser()))
    titles = x1.get_titles(fuzzy_set_parser())

    # tuple_journery = x1.get_tuples(
    #     fuzzy_set_parser(), 'journey_time')
    # tuple_driving = x1.get_tuples(
    #     fuzzy_set_parser(), 'driving')
    # tuple_tip = x1.get_tuples(
    #     fuzzy_set_parser(), 'tip')

    # print(titles)
    # print(tuple_driving)
    # print(tuple_journery)
    # print(tuple_tip)

    # membership = x1.get_titles(
    #     membership_set_parser(),  'membership_')

    # journey_length = membership[0][1]
    # driving_quality = membership[1][1]

    # print('???', membership_set_parser())
    membership = membership_set_parser()

    print('>>? ', membership[0][0])
    # print('journey_length ', membership[1][1])


if __name__ == '__main__':
    main()
