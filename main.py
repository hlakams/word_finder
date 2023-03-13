# necessary imports
from finder import finder

# strings to find
to_find = ['mouse', 'mice']
to_verify = [True, False]

# initial info prompt
print('This program finds the start positions of the words provided in `main.py` as seen in your input string.')

# input string
input_string = input('Enter your input string: ')

# get result
result = finder(input_string, to_find, to_verify)

# find instances + print to console
print('\nStarting locations of given strings to find:')
for idx, result in enumerate(result):
    # no results found
    if len(result) == 0:
        print(f'No results for {to_find[idx]}!')
    # results found
    else:
        print(f'Results for {to_find[idx]}:')
        for value in result:
            print(value)