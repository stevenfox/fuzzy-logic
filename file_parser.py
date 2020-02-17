import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose, assert_raises


file_set = sys.argv[1]
max_n_tuple = sys.argv[2]


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

    def get_tuples(self, dic, title, max_n_tuple=5):
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
        # print(_mem_res)
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

    def defuzzification(self, val_conclusion, _area):
        """
        Defuzzification using centroid (`center of gravity`) method.
        Parameters
        ----------
        x : 1d array, length M
            Independent variable
        mfx : 1d array, length M
            Fuzzy membership function
        Returns
        -------
        u : 1d array, length M
            Defuzzified result
        See also
        --------
        skfuzzy.defuzzify.defuzz, skfuzzy.defuzzify.dcentroid
        """

        '''
        As we suppose linearity between each pair of points of x, we can calculate
        the exact area of the figure (a triangle or a rectangle).
        '''
        temp = []
        mfx = [0.6]
        # for _i in val_conclusion:

        #     temp = [val_conclusion[_i].get('result')]
        #     mfx.append(temp)

        # print('>> ADS', mfx)

        sum_moment_area = 0.0
        sum_area = 0.0

        # If the membership function is a singleton fuzzy set:
        if len(_area) == 1:
            return _area[0]*mfx[0] / np.fmax(mfx[0], np.finfo(float).eps).astype(float)

        # else return the sum of moment*area/sum of area
        for i in range(1, len(_area)):
            x1 = _area[i - 1]
            x2 = _area[i]
            y1 = mfx[i - 1]
            y2 = mfx[i]

            # if y1 == y2 == 0.0 or x1==x2: --> rectangle of zero height or width
            if not(y1 == y2 == 0.0 or x1 == x2):
                if y1 == y2:  # rectangle
                    moment = 0.5 * (x1 + x2)
                    _area = (x2 - x1) * y1
                elif y1 == 0.0 and y2 != 0.0:  # triangle, height y2
                    moment = 2.0 / 3.0 * (x2-x1) + x1
                    _area = 0.5 * (x2 - x1) * y2
                elif y2 == 0.0 and y1 != 0.0:  # triangle, height y1
                    moment = 1.0 / 3.0 * (x2 - x1) + x1
                    _area = 0.5 * (x2 - x1) * y1
                else:
                    moment = (2.0 / 3.0 * (x2-x1) *
                              (y2 + 0.5*y1)) / (y1+y2) + x1
                    _area = 0.5 * (x2 - x1) * (y1 + y2)

                sum_moment_area += moment * _area
                sum_area += _area

        return sum_moment_area / np.fmax(sum_area,
                                         np.finfo(float).eps).astype(float)

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

        # print(_conclusions_list)
        for conclusion in range(len(_conclusions_list)):
            if(_conclusions_list[conclusion][2] > 0):
                # if(_conclusions_list[0][0] in self.get_tuples(fuzzy_set_parser(), _conclusions_list[0][0])):
                _current_tuple = self.get_tuples(
                    fuzzy_set_parser(), _conclusions_list[conclusion][0])
                # print('>>', _current_tuple)
                for _tuple_ in _current_tuple:
                    # print(' dAS >D', _tuple_[0])
                    # print('conc', _conclusions_list[conclusion][1])
                    if(_tuple_[0] == _conclusions_list[conclusion][1]):
                        _tuple_conclusion = _tuple_
                        _a_b = (float(_tuple_[3]) + float(_tuple_[4]))
                        # if _a_b == '0':
                        #     _a_b = (float(_tuple_[2]) + float(_tuple_[3]))
                        _conclusion_value = float(
                            _conclusions_list[conclusion][2])
                        print(_tuple_)
                        # print('ALpha', self.get_alpha(_tuple_, _tuple_[1]))
                        # print('Beta ', self.get_beta(_tuple_, _tuple_[1]))

                        _alpha = int(_tuple_[1]) - int(_tuple_[3])
                        _beta = int(_tuple_[2]) + int(_tuple_[4])
                        _upper_base = int(_tuple_[2]) - int(_tuple_[1])

                        _lower_base = _beta - _alpha

                        print("ALPHA, ", _alpha)
                        print("BETA, ", _beta)
                        print('upper_base:', _upper_base)
                        print('lower_base:', _lower_base)

                        # print('A and B ', _tuple_[2], _tuple_[3], '=', _a_b)
                        # print((0.5 * _conclusion_value * _a_b * _conclusion_value))
                        # print(_a_b, '*', _conclusion_value,
                        #       '=', _a_b * _conclusion_value)

                        _area = round((0.5 * float(_conclusion_value) *
                                       (_lower_base+(_lower_base*(1-_conclusion_value)))), 3)
                        #  area = round(((0.5 * (_upper_base+_lower_base)) - (0.5 *
                        #  float(_conclusion_value) * (float(_a_b) * float(_conclusion_value)))), 3)

                        # _area = round(((0.5 * (_a_b)) - (0.5 *
                        #                                  float(_conclusion_value) * (float(_a_b) * float(_conclusion_value)))), 3)

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

                        print('Centroid: ', _centroid)

                        print(
                            '--------------------------------------------------------')
                        print("Area: ", _area, 'Area centre:', _area_centre, 'for', _conclusion_value,
                              'and', _conclusions_list[conclusion][1])
        print(
            '--------------------------------------------------------')
        print('Defuzzified value: ', np.sum(
            _area_centre_list) / np.sum(_area_list), 'AREA LIST: ', _area_centre_list, '<<')
        print(
            '--------------------------------------------------------')


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
    print('Please wait...')
    fuzzy_ = Fuzzy_set()
    membership = membership_set_parser()

    fuzzy_.defuzzy(fuzzy_.fuzzification())


def main():
    # runall()
    print('\n')
    print('–––––––––––––––––––––––––––––––-------------------–––––––––––----––––––––––––––––––––-–')
    print('File parser and fuzzy logic for the given text file example.')
    print('In order to run it, please run the fuzzy_logic file along with the required arguments')
    print('e.g. $ python fuzzy_logic.py files/RuleSet_complex.txt 6 ')
    print('–––––––––––––––––––––––––––––––-------------------–––––––––––----––––––––––––––––––––-–')
    print('\n')


def gaussmf(x, mean, sigma):
    """
    Gaussian fuzzy membership function.
    Parameters
    ----------
    x : 1d array or iterable
        Independent variable.
    mean : float
        Gaussian parameter for center (mean) value.
    sigma : float
        Gaussian parameter for standard deviation.
    Returns
    -------
    y : 1d array
        Gaussian membership function for x.
    """
    return np.exp(-((x - mean)**2.) / (2 * sigma**2.))


if __name__ == '__main__':
    main()
