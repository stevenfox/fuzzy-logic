# fuzzy-logic

An implementation of a fuzzy-logic rule based system with the use of scikit-fuzzy library and custom file parser

## Description of dictionaries in the parser

### Rule parser set:

Rule: If driving is good and journey is short then tip is big

parser variables:

first_var_i : driving,
first_val_i : good,
operator_i : and,
second_var_i : journey,
second_val_i : short,
result_var_i : tip,
result_val_1 : big
