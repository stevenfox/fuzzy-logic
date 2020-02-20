# fuzzy-logic

An implementation of a fuzzy-logic rule based system with the use of scikit-fuzzy library and custom file parser

## Execution

For the purpose of execution of the fuzzy logic system, there are couple of prerequisite steps need to be taken.
The steps are mentioned below:

1. Have installed the python v3.8 in the environment that is going to be executed. It might work on earlier versions of python. However, it is not recommended as it is tested on v3.8

2. Open a terminal / command window and navigate to the folder where the fuzzy logic system is located. E.g. /Desktop/fuzzy-logic/

3. Have ready the input file that is going to be used for the fuzzification in the proper format. Please follow the format that is shown in the 2 examples in the folder /files

4. On the command / terminal window type in the following three arguments.The name of the file main.py after, the name of the input file and lastly the number of the biggest tuple that exists in your file. If not a number is entered as the third argument, the system will use the default value of maximum set of 5.

For example: \$ python main.py files/RuleSet_complex.txt 6
Please note: the python argument, denotes the python environment to execute the file main.py. However, some environments, e.g. Pycharm, do not need to specify this keyword at the beginning.

5. Observe the generated results from the terminal / command window. The system will output the quantifiable result in Crisp logic, given fuzzy sets and the corresponding membership degrees value.

For more details and documentation about the software, please refer to the assessment in part 2.

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
result_val_i : big
