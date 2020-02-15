import sys
import os
import numpy as np

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

        # elif (_dic_indx < 2):
        # print("No Rules found")

        # print("set\n", rule_set_dict)

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
            # print('len', len(val), val)
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
        # print(fuzzy_set_dict)
            _cnt += 1
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

    def get_tuples(self, dic, title, keytitle='Title_'):
        self.tuple_dict = []
        count = 0
        _end_of_file = 0
        # print('TITLE: ', title)
        # print(dic)
        for key_dic in dic:
            count += 1
            # print('=' in dic[key_dic], dic[key_dic])
            # print('?', key_dic)
            # if(title in dic[key_dic]):
            #     print('title', title)
            if('=' in dic[key_dic]):
                _end_of_file = count
                # print('end of file', _end_of_file, 'dic_len', len(
                # dic.keys()), (int(len(dic.keys()) - _end_of_file)))
                # print('True')
            if keytitle in key_dic:
                # print('>> ', keytitle)
                list_tuple = list(dic.values())
                tuple_title = ' '.join(map(str, dic[key_dic]))
                # print('< > ', tuple_title)
                if(title in str(tuple_title)):
                    _cnt = 0

                    # print('ler', list_tuple)
                    # for a in dic.keys():
                    # if(key_dic > dic.keys):
                    #     count
                    # print('gooxo', a)
                    _space_between_t = 0
                    for m in range(len(list_tuple[count])):
                        if(_end_of_file < count+m and '=' not in list_tuple[count+m]):
                            # print('cnt', count+m)

                            if((len(list_tuple[count+m])) == 1):
                                _space_between_t += 1

                            if _space_between_t < 1:
                                # print('edw', list_tuple[count+m])
                                # print(len(list_tuple[count+m]))
                                # print('-- ', _space_between_t)

                                self.tuple_dict.append(list_tuple[count+m])

                            if(len(self.tuple_dict) < 1):
                                print('No tupple title found')
                                # print('(len(self.tuple_dict)',
                                #   (len(self.tuple_dict)))

                                # return None
        # print(self.tuple_dict)
        return self.tuple_dict
        # print('edw', '=' in list_tuple[count+m])

        #             if(len(list_tuple[count]) != 1):
        #                 for k in range(len(list_tuple[count])):
        #                     for l in list_tuple:
        #                         if(_end_of_file != False):
        #                             # print('list  ', k)

        #                             # if ((k) < 3):
        #                             # print('k ', k)

        #                             # print('(len(list_tuple[count] ',
        #                             #       (len(list_tuple[count+k])))
        #                             print('> _ ) ', list_tuple[count+k])
        #                 if(len(list_tuple[k]) == 1):
        #                     _cnt -= 1
        #                 else:
        #                     _cnt += 1

        #                 for j in range(_cnt):
        #                     if(len(list_tuple[count+j]) > 1):
        #                         self.tuple_dict.append(list_tuple[count+j])
        #             # k = 0

    def get_numbers_tuple(self, dic, _cnt=3):
        # print(max(dic[0][1]))
        self.tuple_int = []
        for k in range(_cnt):
            self.tuple_int.append((dic[k][1:]))
        print(self.tuple_int)
        return self.tuple_int

    def get_beta(self, dic, i):
        return int(dic[i][2]) + int(dic[i][4])

    def get_alpha(self, dic, i):
        return int(dic[i][1]) - int(dic[i][3])

    def membership_calc(self, dic, title, val):
        self.membership_results = {}

        # print('membership: ', dic)
        for s in range(len(dic)):
            # print('\n - - - -Tuple ', dic[s][0])
            # print('- - - -Tuple title ', dic)

            _a = int(dic[s][1])
            _b = int(dic[s][2])
            _a1 = int(dic[s][3])
            _b1 = int(dic[s][4])
            _alpha = self.get_alpha(dic, s)
            _beta = self.get_beta(dic, s)

            if(val < _alpha or val > _beta):
                self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                    0, "given_value": val}})
            # if(val < _alpha):
            #     print('0')
            if(_a <= val and val <= _b):
                print('1')
                self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                    1, "given_value": val}})
            if(val <= _a):
                # if(_a1 != _alpha):
                if(_alpha < val and val < _a):
                    # print('a', _a)
                    # print('  ', (val - _a + _a1) / (float(_a1)))
                    self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                        (val - _a + _a1) / float(_a1), "given_value": val}})
                # if(_b != _b):

            if(val >= _b):
                if(_b1 != _beta):
                    if(_b1 < val and val < _beta):
                        # print('b', _b)
                        # print(' ', (_b + _b1 - val) / float(_b1))
                        self.membership_results.update({s: {'title': title, 'criteria': dic[s][0], 'result':
                                                            (_b + _b1 - val) / float(_b1), "given_value": val}})
        # print(self.membership_results)
        return self.membership_results

    def fuzzification(self, _mem_res):
        # print(_mem_res)
        _rules_parser = rule_set_parser()
        _fparser = fuzzy_set_parser()
        _fset = Fuzzy_set()
        _mem_parser = membership_set_parser()
        _titles = _fset.get_titles(_fparser)

        memb_calc_set = {}
        for j in range(len(_mem_parser)):
            # print('range(len(_mem_parser)', range(len(_mem_parser)))
            for _title in _titles:
                if(str(_title[0]) in _mem_parser[j][0]):
                    _tuple = _fset.get_tuples(_fparser, _title[0])
                    memb_calc_set.update({j: _fset.membership_calc(
                        _tuple, _title[0], int(_mem_parser[j][1]))})

                    # print('pray', _tuple, _title[0], _mem_parser[j][1])
        # print('rules      ',  memb_calc_set)
        print(memb_calc_set)
        # print('rules      ', _mem_res)
        _cnt = 1

        # for _item in _fparser.items():

        # print(_titles[0])
        # print(_rules_parser.keys())
        # for l in memb_calc_set:
        #     print(memb_calc_set[l])
        # _n = 1
        for _m in memb_calc_set:
            # print("\nPerson ID:", p_id)
            # print('> DS', memb_calc_set[1][0].get('criteria'))
            for _n in memb_calc_set[_m]:
                # print('m', _m, 'n', _n)
                for _indx in range((_rules_parser['num_of_rules'])+1):
                    # print('> key', memb_calc_set[_m][_n].get('title') in _rules_parser['first_var_'+str(_indx)] and memb_calc_set[_m][_n].get('criteria') in _rules_parser['first_val_'+str(
                    #     _indx)] and memb_calc_set[_m][_n].get('title') in _rules_parser['second_var_'+str(_indx)] and memb_calc_set[_m][_n].get('criteria') in _rules_parser['second_val_'+str(_indx)])
                    # print('> DS', memb_calc_set)
                    if memb_calc_set[_m][_n].get('title') in _rules_parser['first_var_'+str(_indx)] and memb_calc_set[_m][_n].get('criteria') in _rules_parser['first_val_'+str(_indx)]:
                        print('----->', memb_calc_set[_m][_n].get('title'),
                              '--', memb_calc_set[_m][_n].get('criteria'))

                        for _s in memb_calc_set:
                            for _d in memb_calc_set[_s]:
                                # print(
                                #     ' > >', memb_calc_set[_d][_s].get('criteria'), 's', _s, 'd', _d)
                                if memb_calc_set[_s][_d].get('title') in _rules_parser['second_var_'+str(_indx)] and memb_calc_set[_s][_d].get('criteria') in _rules_parser['second_val_'+str(_indx)]:
                                    print('\t---->', memb_calc_set[_s][_d].get(
                                        'title'),  '--', memb_calc_set[_s][_d].get('criteria'))
                                    if 'and' in _rules_parser['operator_'+str(_indx)]:

                                        print('min of: ', memb_calc_set[_m][_n].get(
                                            'result'), ' - ', memb_calc_set[_s][_d].get('result'))

                                    else:
                                        print('max of: ', memb_calc_set[_m][_n].get(
                                            'result'), ' - ', memb_calc_set[_s][_d].get('result'))
                                    # for _title in _titles:
                                        # if _title[0] in _rules_parser['result_var_'+str(_indx)] and _fparser[0][2] in _rules_parser['result_val_'+str(_indx)]:
                                        # if _title[0] in _rules_parser['result_var_'+str(_indx)]:
                                        #     print('true if ')

        return None
        # for _ascendant in range(len(memb_calc_set[0])):
        #     if memb_calc_set[_ascendant][0][0] in _rules_parser['first_var_'+str(_indx)]:
        #         for _ascendant_2 in range(len(memb_calc_set[0][:])):
        #             if memb_calc_set[1][_ascendant_2][1] in _rules_parser['first_val_'+str(_indx)]:
        #                 for _descendant in range(len(memb_calc_set[0])):
        #                     if memb_calc_set[_descendant][0][0] in _rules_parser['second_var_'+str(_indx)]:
        #                         for _descendant_2 in range(len(memb_calc_set[0])):
        #                             if memb_calc_set[0][_descendant_2][1] in _rules_parser['second_val_'+str(_indx)]:
        #                                 if 'and' in _rules_parser['operator_'+str(_indx)]:
        #                                     print('and min()',
        #                                           memb_calc_set[1][0][0])
        #                                 else:
        #                                     print('or max()',
        #                                           memb_calc_set[0][0][0])
        #                                 for _title in _titles:
        #                                     # if _title[0] in _rules_parser['result_var_'+str(_indx)] and _fparser[0][2] in _rules_parser['result_val_'+str(_indx)]:
        #                                     if _title[0] in _rules_parser['result_var_'+str(_indx)]:
        #                                         print('true if ')


def trap_membership_calc(mem_val, dic, _pos=0):
    """
    Trapezoidal membership function generator.
    Parameters
    ----------
    x : 1d array
        Independent variable.
    abcd : 1d array, length 4
        Four-element vector.  Ensure a <= b <= c <= d.
    Returns
    -------
    y : 1d array
        Trapezoidal membership function.
    """

    _fs = Fuzzy_set()
    maxLength = max(map(len, dic))

    tuple_values = []
    val_list = []

    # abcd = [30, 50, 50, 70]

    for s in range((maxLength)):
        tuple_values.append(dic[_pos][s])

    # print('> ', tuple_values)
    # print('abdcd', abcd[0][1])
    # for i in dic:
    # print('i    >  ', i)
    # # abcd.append(i[0])
    # print('abscs > ', abcd)

    abcd = [_fs.get_alpha(dic, _pos), int(tuple_values[1]),
            int(tuple_values[2]), _fs.get_beta(dic, _pos)]
    print('abcd >> > ', abcd)
    assert len(abcd) == 4, 'abcd parameter must have exactly four elements.'
    _alpha, _a, _b, _beta = np.r_[abcd]
    a_x = [mem_val]
    x = np.array(a_x)
    # print('??', _alpha, _a, _b, _beta)
    assert _alpha <= _a and _a <= _b and _b <= _beta, 'abcd requires the four elements \
                                          _alpha <= _a <= _b <= _beta.'
    y = np.ones(len(x))

    idx = np.nonzero(x <= _a)[0]
    y[idx] = trimf(x[idx], np.r_[_alpha, _a, _a], tuple_values, mem_val)

    idx = np.nonzero(x >= _b)[0]
    print('_ <', idx)
    y[idx] = trimf(x[idx], np.r_[_b, _b, _beta], tuple_values, mem_val)

    idx = np.nonzero(x < _alpha)[0]
    y[idx] = np.zeros(len(idx))

    idx = np.nonzero(x > _beta)[0]
    y[idx] = np.zeros(len(idx))

    return y


def trimf(x, abc, _list, _mem_val):
    """
    Triangular membership function generator.
    Parameters
    ----------
    x : 1d array
        Independent variable.
    abc : 1d array, length 3
        Three-element vector controlling shape of triangular function.
        Requires a <= b <= c.
    Returns
    -------
    y : 1d array
        Triangular membership function.
    """
    assert len(abc) == 3, 'abc parameter must have exactly three elements.'
    a, b, c = np.r_[abc]     # Zero-indexing in Python
    assert a <= b and b <= c, 'abc requires the three elements a <= b <= c.'
    _ba = 9
    y = np.zeros(len(x))

    # print('abc : ,', abc)
    # Left side
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)
        # y[idx] = (x[idx] - a + b) / float(b)
        print('in a: ', (_mem_val -
                         int(_list[1]) + int(_list[3])) / (float(_list[3])))

    # Right side
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
        # y[idx] = (b + c - x[idx]) / float(c)
        print('> > > in b:',
              (int(_list[2]) + int(_list[4]) - _mem_val) / float(_list[4]))

    idx = np.nonzero(x == b)
    y[idx] = 1
    return y


def runall():
    fuzzy_ = Fuzzy_set()
    membership = membership_set_parser()

    all_tuples = []
    tuples = fuzzy_.get_titles(fuzzy_set_parser())
    # tuples_set = fuzzy_s.get_tuples(fuzzy_set_parser(), 'tip')

    # print(tuples)
    _cnt = 0
    # print('> L ', len(membership))
    for i in tuples:
        if(i != (tuples[0])):
            # print(i[0])
            tuples_set = fuzzy_.get_tuples(
                fuzzy_set_parser(), i[0])
            all_tuples.append(tuples_set)
            fuzzy_.fuzzification(all_tuples)

    # for j in all_tuples:

        # print(trap_membership_calc(int(membership[i][1]), j, 1))
        # print(fuzzy_.membership_calc(j, int(membership[0][1])))

    # print(j)

    # # print(i not in tuples[0], i, tuples[0])
    # # print(*tuples[i])
    # print(': P ', all_tuples[1][0][1])


def main():
    #  rules
    # rules_set = rule_set_parser()
    # print('rules      ', rules_set['operator_2'])

    #  fuzzy set
    fuzzy_s = Fuzzy_set()

    # print(fuzzy_s.add(fuzzy_set_parser()))

    titles = fuzzy_s.get_titles(fuzzy_set_parser())

    # tuple_driving = fuzzy_s.get_tuples(
    #     fuzzy_set_parser(), 'driving')

    # print(fuzzy_set_parser())
    tuple_journery = fuzzy_s.get_tuples(
        fuzzy_set_parser(), 'journey_time')
    # tuple_resp = fuzzy_s.get_tuples(
    #     fuzzy_set_parser(), 'rerspiration_rate')
    # tuple_tip = fuzzy_s.get_tuples(
    #     fuzzy_set_parser(), 'tip')

    # print(titles[1][0])
    # print('individual values ', tuple_driving[2][1])
    # print(tuple_journery)
    tuples = fuzzy_s.get_titles(fuzzy_set_parser())
    # print(tuple_driving)
    # print(tuple_journery)

    # print(tuple_tip)

    # _a = tuple_driving[2][1]
    # _b = tuple_driving[2][2]
    # _c = tuple_driving[2][3]
    # _d = tuple_driving[2][4]
    # print(fuzzy_s.get_beta(tuple_driving, 1))

# ---- membership
    membership = membership_set_parser()
    # print('membership: ', membership[0][0],
    #       '| value:', int(membership[0][1]))
    # journey_length = membership[0][1]
    # driving_quality = membership[1][1]

    # print(fuzzy_s.membership_calc(tuple_driving, int(membership[1][1])))
    # print(fuzzy_s.membership_calc(tuple_journery, int(membership[0][1])))
    _memres = fuzzy_s.membership_calc(
        tuple_journery, 'journey_time', int(membership[0][1]))
    # print(tuple_journery, 'journe, y_time')
    # print(fuzzy_s.membership_calc(tuple_resp, int(membership[0][1])))

    # print(trap_membership_calc(int(membership[1][1]), tuple_driving, 1))
    # print(trap_membership_calc(int(membership[0][1]), tuple_journery, 1))

    # print('mem results: ', _memres)

    fuzzy_s.fuzzification(_memres)

    # print(tuples[0][])
    # print(tuples)

    # print(str(tuples).lstrip('[').rstrip(']'))
    # print(tuples[0])

    # tuples_set = fuzzy_s.get_tuples(fuzzy_set_parser(), 'tip')
    # all_tuples = []
    # for i in tuples:
    #     if(i != (tuples[0])):
    #         # print(i[0])
    #         tuples_set = fuzzy_s.get_tuples(
    #             fuzzy_set_parser(), i[0])
    #         all_tuples.append(tuples_set)

    # for j in all_tuples:

    #     # print(trap_membership_calc(int(membership[i][1]), j, 1))
    #     # fuzzy_s.fuzzification()
    # print(fuzzy_s.membership_calc(j, int(membership[0][1])))
    # runall()
    # print(j)

    # # # print(i not in tuples[0], i, tuples[0])
    # # # print(*tuples[i])
    # print(': P ', all_tuples[1][0][1])
    # for j in tuples_set:
    #     print(j)


if __name__ == '__main__':
    main()
