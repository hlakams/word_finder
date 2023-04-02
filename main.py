# necessary imports
from finder import finder

# strings to find
to_find = ['mouse', 'mice']
to_verify = [True, False]

# initial info prompt
print('This program finds the start positions of the words provided in `main.py` as seen in your input string.')
# check if user wants custom strings to find
custom_find = input('Do you want to use the default strings to find [Y/n]? ')
find_verify = ['yes', 'y', '']

# add strings to find
if custom_find.lower().strip() not in find_verify:
    # remove old strings
    to_find.clear()
    to_verify.clear()
    custom_find = ''
    # keep adding strings to find
    while custom_find.lower().strip() in find_verify:
        # new string
        new_find = input('\nEnter a custom string to find: ')
        to_find.append(new_find)

        # singular find condition
        new_verify = input('Do you want to find singular instances only (substrings by default) [Y/n]? ')
        if new_verify in find_verify:
            to_verify.append(True)
        else:
            to_verify.append(False)

        # prompt user for more strings
        custom_find = input('Do you want add more custom strings to find [Y/n]? ')

# input string
input_string = input('\nEnter your input string: ')

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
