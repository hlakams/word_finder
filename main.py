# necessary imports
from finder import finder

# strings to find
to_find = ['mouse', 'mice']

# input string
input_string = input('Enter your input string: ')

# find instances + print to console
print('\nStarting locations of given input strings:')
for idx in finder(input_string, to_find):
    print(idx)