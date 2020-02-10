import sys
import os


file_set = 'files/RuleSet.txt'


def readFile():
    _filepath = file_set
    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()
    _lines = open(file_set).readlines()
    return _lines


def search(values, searchFor, list_index):
    # print('search: ', values, searchFor, list_index)
    list_values = values.split()
    for i in list_values:
        if searchFor in i:
            return list_values[list_index]
    return None


def rule_set_parser():
    _lines = readFile()
    rule_dict = {}

    for l in _lines:
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
            _dic_indx += 1

        elif (_dic_indx < 2):
            print("No Rules found")

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

    def max_tuple(self, dic, i):
        return int(dic[i][2]) + int(dic[i][4])

    def min_tuple(self, dic, i):
        return int(dic[i][1]) - int(dic[i][3])


def fuzzy_set_parser():

    _lines = readFile()
    fuzzy_dict = {}
    f_set = Fuzzy_set()
    counter = 0

    for l in _lines:
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

    _lines = readFile()
    membership_dict = {}
    counter = 0
    membership_set_dict = []
    for l in _lines:
        if '=' in l:
            str_l = l.replace('=', '')
            val = str_l.split()
            membership_dict[counter] = val
            counter += 1

    return membership_dict


def main():
    #  rules
    rules_set = rule_set_parser()
    # print('rules      ', rules_set)

#  fuzzy set
    fuzzy_s = Fuzzy_set()

    # print(fuzzy_s.add(fuzzy_set_parser()))

    titles = fuzzy_s.get_titles(fuzzy_set_parser())

    tuple_driving = fuzzy_s.get_tuples(
        fuzzy_set_parser(), 'driving')
    tuple_journery = fuzzy_s.get_tuples(
        fuzzy_set_parser(), 'journey_time')
    tuple_tip = fuzzy_s.get_tuples(
        fuzzy_set_parser(), 'tip')

    # print(titles[1][0])
    print('individual values ', tuple_driving[1][3])
    # print(tuple_journery)
    # print(tuple_tip)

    print(fuzzy_s.max_tuple(tuple_driving, 1))

# ---- membership
    membership = membership_set_parser()
    print('membership: ', membership[0][0],
          '| value:', int(membership[0][1]))
    # journey_length = membership[0][1]
    # driving_quality = membership[1][1]


if __name__ == '__main__':
    main()
