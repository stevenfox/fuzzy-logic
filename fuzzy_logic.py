import file_parser as fp
from file_parser import Fuzzy_set as Fuzzy_set
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from operator import itemgetter


# New Antecedent/Consequent objects hold universe variables and membership
# functions

fset = Fuzzy_set()
# fp.fuzzy_set_parser()

# fuzzy_set_dic = fp.fuzzy_set_parser()


f_titles = fset.get_titles(fp.fuzzy_set_parser())


# print(f_titles[1])

tuple_journ = fset.get_tuples(
    fp.fuzzy_set_parser(), 'JourneyLength')

min_journey_str = ((min(tuple_journ[0][1:]).replace('(', '')))
min_journey = int(min_journey_str.replace(',', ''))
max_journey = int((max(tuple_journ[0][1:]).replace(')', '')))


# -- - - -

tuple_driving = fset.get_tuples(fp.fuzzy_set_parser(), 'DrivingQuality')

min_driving_str = ((min(tuple_driving[0][1:]).replace('(', '')))
min_driving = int(min_driving_str.replace(',', ''))
# max_driving = int((max(tuple_driving[0][1:]).replace(')', '')))

# print(min_driving, max_driving)
print(min_driving)


# tuple_tip = fset.get_tuples(
#     fp.fuzzy_set_parser(), 'SizeOfTip')

# results = list(map(int, results))


membership = fset.get_titles(
    fp.membership_set_parser(),  'membership_')

journey_length = membership[0][1]
driving_quality = membership[1][1]

# print(journey_length)


journey_len = ctrl.Antecedent(
    np.arange(min_journey, max_journey, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 100, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 100, 1), 'tip')


# Auto-membership function population is possible with .automf(3, 5, or 7)
journey_len.automf(3)
service.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# You can see how these look with .view()
journey_len['average'].view()
