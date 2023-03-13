# necessary imports
from finder import finder

# strings to find
to_find = ['mouse', 'mice']

# initial info prompt
print('This program finds the start positions of the words provided in `main.py` as seen in your input string.')

# input string
input_string = input('Enter your input string: ')

# find instances + print to console
print('\nStarting locations of given input strings:')
for idx in finder(input_string, to_find):
    print(idx)