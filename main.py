# necessary imports
from finder import finder

# strings to find
to_find = ['mouse', 'mice']

# initial info prompt
print('This program finds the start positions of the words provided in `main.py` as seen in your input string.')

# input string
input_string = input('Enter your input string: ')

# get result
result = finder(input_string, to_find)

# find instances + print to console
print('\nStarting locations of given input strings:')
for idx, result in enumerate(result):
    print(f'Results for {to_find[idx]}:')
    for value in result:
        print(value)