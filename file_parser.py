import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose, assert_raises


file_set = sys.argv[1]
try:
    max_n_tuple = sys.argv[2]
except:
    max_n_tuple = 5
    print('\n\n')
    print('–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ')
    print('No max fussy set number was entered. ')
    print('The system will run with the default value of max 5 fussy set ')
    print('–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ')
    print('\n\n')


def readFile():
    _filepath = file_set
    if not os.path.isfile(_filepath):
        print("File path {} does not exist. Exiting...".format(_filepath))
        sys.exit()
    _lines = open(file_set).readlines()
    return _lines


def search(values, searchFor, list_index):
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

    _dic_indx = 0
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
            rule_set_dict.update(
                {'num_of_rules': int(_dic_indx)})
            _dic_indx += 1
    return rule_set_dict


def fuzzy_set_parser():

    _lines = readFile()
    fuzzy_dict = {}
    f_set = Fuzzy_set()
    counter = 0

    for l in _lines:
        val = l.split()
        if('Rule' not in val):
            fuzzy_dict[counter] = val
            counter += 1
    _cnt = 0
    fuzzy_set_dict = {}
    _tupple_indx = 1
    for i in fuzzy_dict:

        if(len(fuzzy_dict[i]) > 1):
            fuzzy_set_dict.update(
                {'Tuple_'+str(_cnt)+'_'+str(_tupple_indx): fuzzy_dict[i]})
            _tupple_indx += 1
        elif (len(fuzzy_dict[i]) == 1):
            fuzzy_set_dict.update(
                {'Title_'+str(_cnt): fuzzy_dict[i]})
            _tupple_indx = 1
            _cnt += 1
    # print(fuzzy_set_dict)
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


class Fuzzy_set:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def get(self):
        return self.data

    def get_titles(self, dic, keytitle='Title_'):
        self.title_dict = []
        for key_dic in dic:
            if keytitle in key_dic:
                self.title_dict.append(dic[key_dic])
        return self.title_dict

    def get_tuples(self, dic, title, max_n_tuple):
        keytitle = 'Title_'
        self.tuple_dict = []
        count = 0
        _end_of_file = 0
        for key_dic in dic:
            count += 1
            if('=' in dic[key_dic]):
                _end_of_file = count
            if keytitle in key_dic:
                list_tuple = list(dic.values())
                tuple_title = ' '.join(map(str, dic[key_dic]))
                if(title == str(tuple_title)):
                    _cnt = 0
                    _space_between_t = 0
                    for m in range(max_n_tuple):
                        if(_end_of_file < count+m and '=' not in list_tuple[count+m]):
                            if((len(list_tuple[count+m])) == 1):
                                _space_between_t += 1

                            if _space_between_t < 1:
                                self.tuple_dict.append(list_tuple[count+m])

        # print(self.tuple_dict)
        return self.tuple_dict

    def get_numbers_tuple(self, dic, _cnt=3):
        self.tuple_int = []
        for k in range(_cnt):
            self.tuple_int.append((dic[k][1:]))
        return self.tuple_int

    def get_beta(self, dic, i):
        return int(dic[i][2]) + int(dic[i][4])

    def get_alpha(self, dic, i):
        return int(dic[i][1]) - int(dic[i][3])

    def membership_calc(self, dic, title, val):
        self.membership_results = {}

        for s in range(len(dic)):

            _a = int(dic[s][1])
            _b = int(dic[s][2])
            _a1 = int(dic[s][3])
            _b1 = int(dic[s][4])
            _alpha = self.get_alpha(dic, s)
            _beta = self.get_beta(dic, s)

            if(val < _alpha or val > _beta):
                self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                    0, "given_value": val}})
            if(_a <= val and val <= _b):
                self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                    1, "given_value": val}})
            if(val <= _a):
                if(_alpha < val and val < _a):
                    self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                        (val - _a + _a1) / float(_a1), "given_value": val}})
            if(val >= _b):
                if(_b1 != _beta):
                    if(_b1 < val and val < _beta):

                        self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                            (_b + _b1 - val) / float(_b1), "given_value": val}})
        # print(self.membership_results)
        return self.membership_results

    def fuzzification(self):
        _rules_parser = rule_set_parser()
        _fparser = fuzzy_set_parser()
        _fset = Fuzzy_set()
        _mem_parser = membership_set_parser()
        _titles = _fset.get_titles(_fparser)
        _titles.pop(0)
        self.value_conclusion = {}
        conclusions_list = []

        memb_calc_set = {}

        for r in range(len(_titles)):
            for j in range(len(_mem_parser)):
                if(_mem_parser[j][0] == str(_titles[r][0])):
                    _tuple = _fset.get_tuples(
                        _fparser, _mem_parser[j][0], int(max_n_tuple))
                    memb_calc_set.update({j: _fset.membership_calc(
                        _tuple, _mem_parser[j][0], int(_mem_parser[j][1]))})

        _cnt = 1
        for _m in memb_calc_set:
            for _n in memb_calc_set[_m]:
                for _indx in range((_rules_parser['num_of_rules'])+1):
                    if memb_calc_set[_m][_n].get('title') == _rules_parser['first_var_'+str(_indx)] and memb_calc_set[_m][_n].get('criteria') == _rules_parser['first_val_'+str(_indx)]:
                        _kn = 0
                        for _s in memb_calc_set:
                            _kn += 1
                            for _d in memb_calc_set[_s]:
                                if memb_calc_set[_s][_d].get('title') == _rules_parser['second_var_'+str(_indx)] and memb_calc_set[_s][_d].get('criteria') == _rules_parser['second_val_'+str(_indx)]:
                                    if 'and' == _rules_parser['operator_'+str(_indx)]:
                                        _min_val = min(memb_calc_set[_m][_n].get(
                                            'result'), memb_calc_set[_s][_d].get('result'))
                                        self.value_conclusion.update({_n: {'value': _min_val, 'result_name': _rules_parser['result_var_'+str(
                                            _indx)], 'conclusion': _rules_parser['result_val_'+str(_indx)]}})
                                        conclusions_list.append(
                                            [_rules_parser['result_var_'+str(_indx)], _rules_parser['result_val_'+str(_indx)], _min_val])

                                    else:
                                        _max_val = max(memb_calc_set[_m][_n].get(
                                            'result'), memb_calc_set[_s][_d].get('result'))

                                        self.value_conclusion.update({_n: {'value': _max_val,  'result_name': _rules_parser['result_var_'+str(
                                            _indx)], 'conclusion': _rules_parser['result_val_'+str(_indx)]}})

                                        conclusions_list.append([_rules_parser['result_var_'+str(_indx)], _rules_parser['result_val_'+str(
                                            _indx)], _max_val, memb_calc_set[_m][_n].get('result')])

        # return self.value_conclusion
        return conclusions_list

    def defuzzy(self, _conclusions):

        _area_list = []
        _area_centre_list = []
        _area_centre = 0
        _area = 0
        # convert list of list into list of tuple
        tuple_line = [tuple(pt) for pt in _conclusions]
        # remove duplicated element
        tuple_new_line = sorted(set(tuple_line), key=tuple_line.index)
        # convert list of tuple into list of list
        _conclusions_list = [list(t) for t in tuple_new_line]

        for conclusion in range(len(_conclusions_list)):
            if(_conclusions_list[conclusion][2] > 0):
                _current_tuple = self.get_tuples(
                    fuzzy_set_parser(), _conclusions_list[conclusion][0], int(max_n_tuple))
                for _tuple_ in _current_tuple:
                    if(_tuple_[0] == _conclusions_list[conclusion][1]):
                        _tuple_conclusion = _tuple_
                        _a_b = (float(_tuple_[3]) + float(_tuple_[4]))
                        _alpha = int(_tuple_[1]) - int(_tuple_[3])
                        _beta = int(_tuple_[2]) + int(_tuple_[4])
                        _upper_base = int(_tuple_[2]) - int(_tuple_[1])
                        _lower_base = _beta - _alpha
                        _conclusion_value = round(float(
                            _conclusions_list[conclusion][2]), 3)

                        _area = round((0.5 * _conclusion_value *
                                       (_lower_base+(_lower_base*(1-_conclusion_value)))), 3)

                        if (int(_tuple_[1])) == (int(_tuple_[2])):

                            _mid_point = _alpha + (_lower_base/2)
                            _centroid = int(
                                _tuple_[1]) + ((_mid_point - int(_tuple_[1])) * 2 / 3)

                        else:
                            _centroid = (
                                ((2 * _lower_base + _upper_base) / (3 * (_lower_base + _upper_base))*_conclusion_value))

                        _area_list.append(_area)
                        _area_centre = (_area * _centroid)
                        _area_centre_list.append(_area_centre)

                        print('\n')
                        print(
                            '---------------------BEGIN---**--TABLE--------------------')
                        print("ALPHA, ", _alpha)
                        print("BETA, ", _beta)
                        print('upper_base:', _upper_base)
                        print('lower_base:', _lower_base)
                        print('Centroid: ', _centroid)

                        print(
                            '--------------------------------------------------------')
                        print("Area: ", _area, 'Area centre:', _area_centre, 'for membership value of', _conclusion_value,
                              'and conclusion', _conclusions_list[conclusion][1])
                        print(
                            '--------------------------------------------------------')
        print(
            '--------------------------------------------------------')
        print('Defuzzified value: ', round(np.sum(
            _area_centre_list) / np.sum(_area_list), 5))
        print(
            '--------------------------------------------------------')


def runall():
    print('Please wait...')
    fuzzy_ = Fuzzy_set()
    membership = membership_set_parser()

    fuzzy_.defuzzy(fuzzy_.fuzzification())


def main():
    # runall()
    print('\n')
    print('–––––––––––––––––––––––––––––––-------------------–––––––––––----––––––––––––––––––––-–')
    print('| File parser and fuzzification logic file.                                            |')
    print('| In order to run it, please run the main file along with the required arguments       |')
    print('| e.g. $ python main.py files/RuleSet_complex.txt 6                                    |')
    print('–––––––––––––––––––––––––––––––-------------------–––––––––––----––––––––––––––––––––-–')
    print('\n')


if __name__ == '__main__':
    main()
